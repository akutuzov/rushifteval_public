#! /bin/env/ python3

import os
from argparse import ArgumentParser
from gensim.models import KeyedVectors
import logging
from scipy.spatial.distance import cosine

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO
    )

    parser = ArgumentParser()
    parser.add_argument(
        "--embeddings_dir",
        "-e",
        required=True,
        help="Path to the directory with pre-trained embeddings",
        action="store",
    )
    parser.add_argument(
        "--wordlist",
        "-w",
        required=True,
        help="Path to the file with the list of words",
        action="store",
    )
    args = parser.parse_args()

    models = ["pre-soviet_lemmas.bin", "soviet_lemmas.bin", "post-soviet_lemmas.bin"]

    emb1, emb2, emb3 = [
        KeyedVectors.load_word2vec_format(
            os.path.join(args.embeddings_dir, model), binary=True
        )
        for model in models
    ]
    common_vocab = emb1.vocab.keys() & emb2.vocab.keys() & emb3.vocab.keys()

    words = open(args.wordlist, "r").readlines()

    with open("answer.tsv", "w") as out:
        for word in words:
            word = word.strip()
            word_noun = word + "_NOUN"

            n1 = [n[0] for n in emb1.most_similar(word_noun)]
            n2 = [n[0] for n in emb2.most_similar(word_noun)]
            n3 = [n[0] for n in emb3.most_similar(word_noun)]

            neighbors = [w for w in (set(n1) | set(n2) | set(n3)) if w in common_vocab]

            v1 = [emb1.similarity(word_noun, n) for n in neighbors]
            v2 = [emb2.similarity(word_noun, n) for n in neighbors]
            v3 = [emb3.similarity(word_noun, n) for n in neighbors]

            out.write(
                f"{word}\t{1 - cosine(v1, v2)}\t{1 - cosine(v2, v3)}\t{1 - cosine(v1, v3)}\n"
            )
