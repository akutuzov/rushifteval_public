# RuShiftEval public data

This repository contains public data and code for the [RuShiftEval'21 shared task](http://www.dialog-21.ru/media/5296/pivovarovalpluskutuzova151.pdf).
The shared task aimed at evaluating the abilities of the existing NLP systems to detect the degree of diachronic semantic change for Russian nouns.

- Join [our Telegram channel](https://t.me/rushifteval)
- Download [pre-trained word2vec embeddings](https://competitions.codalab.org/competitions/28340#participate-get_data) for time-specific Russian corpora

The shared task is now officially finished.

We are publishing the gold annotations and the leaderboard scores:

## Data
RuShiftEval dataset features semantic change scores for three time periods (more details in the [paper](http://www.dialog-21.ru/media/5296/pivovarovalpluskutuzova151.pdf)):

- pre-Soviet VS Soviet (RuShiftEval-1)
- Soviet VS post-Soviet (RuShiftEval-2)
- pre-Soviet VS post-Soviet (RuShiftEval-3)

- `annotated_devset.tsv`: gold semantic change estimations for the Development phase (aggregation of manually annotated data)
- `annotated_testset.tsv`: gold semantic change estimations for the Evaluation phase (aggregation of manually annotated data)
- `leaderboard_results.tsv`:  a list of all Evaluation phase submissions with their corresponding scores.

The `raw_annotations` directory contains raw per-sentence annotator judgments.

### Inter-rater agreement
*Test set*

|              | Krippendorff's alpha | Spearman rho |
|--------------|----------------------|--------------|
| RuShiftEval-1|  0.506               | 0.521        |
| RuShiftEval-2|  0.549               | 0.559        |
| RuShiftEval-3|  0.544               | 0.556        |


*Development set*

|              | Krippendorff's alpha | Spearman rho |
|--------------|----------------------|--------------|
| RuShiftEval-1|  0.592               | 0.613        |
| RuShiftEval-2|  0.609               | 0.627        |
| RuShiftEval-3|  0.597               | 0.632        |



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


