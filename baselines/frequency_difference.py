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

    total1, total2, total3 = [
        sum([emb.vocab[w].count for w in emb.vocab])
        for emb in [emb1, emb2, emb3]
        ]

    print(total1, total2, total3)
    
    words = open(args.wordlist, "r").readlines()

    
    with open("answer.tsv", "w") as out:
        for word in words:
            word = word.strip()
            word_noun = word + "_NOUN"
                        
            f1 = emb1.vocab[word+"_NOUN"].count / float(total1)
            f2 = emb2.vocab[word+"_NOUN"].count / float(total2)
            f3 = emb3.vocab[word+"_NOUN"].count / float(total3)
            
            out.write(
                f"{word}\t{1 - abs(f1-f2)}\t{1 - abs(f2-f3)}\t{1 - abs(f1-f3)}\n"
            )
