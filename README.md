# RuShiftEval public data

This repository contains public data and code for the [RuShiftEval'21 shared task](https://competitions.codalab.org/my/competition/28340).
The shared task aimed at evaluating the abilities of the existing NLP systems to detect the degree of diachronic semantic change for Russian nouns.

- Join [our Telegram channel](https://t.me/rushifteval)
- Download [pre-trained word2vec embeddings](https://competitions.codalab.org/competitions/28340#participate-get_data) for time-specific Russian corpora

The shared task is now officially finished.
We are publishing the gold annotations and the leaderboard scores:

## Data
- `annotated_devset.tsv`: gold semantic change estimations for the Development phase (aggregation of manually annotated data)
- `annotated_testset.tsv`: gold semantic change estimations for the Evaluation phase (aggregation of manually annotated data)
- `leaderboard_results.tsv`:  a list of all Evaluation phase submissions with their corresponding scores.

The `raw_annotations` directory contains raw per-sentence annotator judgments.


## Starting kits

In this directory, you will find submission templates for different phases of the shared task:
- Practice phase
- Development phase
- Evaluation phase (will be published after February 22)

In particular, the templates provide you with the target words for which semantic change scores have to be predicted.

## Baselines

In this directory, you will find code for various baseline approaches for semantic change detection.

- `local_neighborhood.py`: the local neighborhood method from [Hamilton et al 2016](https://www.aclweb.org/anthology/D16-1229/)
- ...


