# __RuShiftEval-1__: Semantic Change Dataset for Russian


### Type

Dataset

### Authors

Andrey Kutuzov, Lidia Pivovarova

### Description

This data collection contains diachronic semantic relatedness judgments for Russian word usage pairs.

It compares word usages from the pre-Soviet (1700-1916) and Soviet (1918-1990) times.

This is one of three semantic change datasets for Russian published at the [Git repository](https://github.com/akutuzov/rushifteval_public).

This dataset was annotated in a crowd-working effort with hundreds of annotators.
Therefore, pairwise inter-rater agreement scores are meaningless and are not provided.
This also means that the same annotator name may correspond to a different person for two different use pairs. 
E.g. the judgment of annotator1 for two different use pairs could be done by a different person.

- Version 2.0.0 of the data set was an update of the original RuShiftEval shared task data set. The annotated data remains the same, but the following points differ:
  * we change the data format to be compatible with [WUG data sets](https://www.ims.uni-stuttgart.de/data/wugs),
  * missing target word indices are inferred with [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/),
  * punctuation at the beginning or end of target words are excluded from target word indices,
  * change scores are calculated with the code from the [WUG repository](https://github.com/Garrafao/WUGs). This code first aggregates judgments of use pairs with the median over all annotators and then averages all the scores for the measures EARLIER, LATER, COMPARE. Hence, the change scores slightly differ from the ones in the original shared task.

As described in the paper below, the data was further optimized for the CoMeDi shared task. Version 2.0.1 reflects some of the changes described in the paper, i.e., correction of target word and target sentence indices, plus minor additional changes.

Please find more information on the provided data in the papers referenced below.

Version: 2.0.1, 11.1.2025. WUG version. Correct target word and target sentence indices. Map judgment identifiers to use identifiers. Remove 'nan' judgments. Update plots. Add compare plots.

### Reference
Andrey Kutuzov, Lidia Pivovarova. 2021 [Three-part diachronic semantic change dataset for Russian](https://aclanthology.org/2021.lchange-1.2/). 
In Proceedings of the 2nd International Workshop on Computational Approaches to Historical Language Change 2021.

Dominik Schlechtweg, Tejaswi Choppa, Wei Zhao, Michael Roth. 2025. [The CoMeDi Shared Task: Median Judgment Classification & Mean Disagreement Ranking with Ordinal Word-in-Context Judgments](https://aclanthology.org/2025.comedi-1.4/). In Proceedings of the 1st Workshop on Context and Meaning--Navigating Disagreements in NLP Annotations.
