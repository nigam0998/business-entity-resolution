# Business Entity Resolution

## Abstract

This project develops a business entity resolution system for identifying
whether records from different datasets refer to the same real-world business.

The proposed pipeline combines candidate generation, token-based blocking,
address-based blocking, exact-name matching, feature engineering, and
Logistic Regression classification.

The final model achieved an F1-score of 78.38%, with precision of 73.55%
and recall of 83.88% at an optimized probability threshold of 0.95.

## 1. Introduction

Entity resolution identifies records that represent the same real-world
entity across different datasets. Business records may contain variations
in names, addresses, formatting, abbreviations, and other attributes.

This project addresses this problem using a multi-stage entity resolution
pipeline.

## 2. Methodology

The system consists of:

1. Data preprocessing
2. Candidate generation
3. Token-based blocking
4. Address-based blocking
5. Exact-name blocking
6. Feature engineering
7. Logistic Regression classification
8. Threshold optimization
9. Error analysis

### Feature Engineering

The model uses:

- Name similarity
- Name token similarity
- Address similarity
- Address token similarity
- Name Jaccard similarity
- Address Jaccard similarity
- Country matching
- Exact-name matching
- Shared-token information
- Candidate rank

### Classification

A balanced Logistic Regression classifier was used with:

- class_weight = balanced
- max_iter = 1000
- random_state = 42

## 3. Experimental Setup

### Training

- Pairs: 71,092
- Positive: 999
- Negative: 70,093

### Validation

- Pairs: 17,364
- Positive: 242
- Negative: 17,122

### Test

- Pairs: 17,364
- Positive: 242
- Negative: 17,122

## 4. Final Results

The optimized classification threshold was 0.95.

| Metric | Result |
|---|---:|
| Accuracy | 99.35% |
| Precision | 73.55% |
| Recall | 83.88% |
| F1-score | 78.38% |
| Threshold | 0.95 |

### Confusion Matrix

The final confusion matrix was:

[[17049, 73],
 [39, 203]]

## 5. Candidate Generation

The final candidate-generation experiment evaluated 500 source entities.

- Gold matches: 1,778
- Retrieved gold matches: 1,398
- Candidate recall: 78.63%
- Average final candidates/source: 500.86
- Maximum final candidates/source: 2,363

Therefore, 78.63% of the gold-standard matches were included in the
candidate pool.

## 6. Threshold Analysis

The threshold analysis showed that increasing the threshold improved
precision while reducing recall.

The best F1-score was obtained at threshold 0.95:

- Precision: 73.55%
- Recall: 83.88%
- F1: 78.38%

Therefore, 0.95 was selected as the final operating threshold.

## 7. Missing Candidate Analysis

The missing-candidate analysis identified 496 genuine candidate pairs.

Of these:

- 328 had zero generated candidates.
- 168 had candidates generated but the genuine target was absent.

Exact-name blocking recovered 85 of the 328 zero-candidate cases,
giving an exact-name recovery rate of 25.91%.

## 8. Discussion

The results demonstrate that combining multiple blocking strategies with
supervised classification provides an effective approach to business
entity resolution.

The final classifier achieved strong recall while maintaining reasonable
precision.

Candidate generation remains an important limitation because a genuine
pair that is excluded during blocking cannot be recovered by the
downstream classifier.

## 9. Limitations

The principal limitation is candidate-generation recall. The final
candidate recall was 78.63%, meaning that some genuine matches were
excluded before classification.

The dataset is also highly imbalanced, requiring balanced class weights.

## 10. Future Work

Future improvements could include:

- More sophisticated blocking strategies
- Phonetic name matching
- Character-level similarity
- Geographic similarity
- Transformer-based embeddings
- Learning-to-rank approaches
- Improved handling of missing candidate pairs
- Larger validation datasets

## 11. Conclusion

The developed entity resolution pipeline successfully combines blocking,
similarity features, exact-name matching, and supervised classification.

The final Logistic Regression model achieved:

- Precision: 73.55%
- Recall: 83.88%
- F1-score: 78.38%
- Accuracy: 99.35%

at an optimized threshold of 0.95.

The candidate-generation stage achieved 78.63% recall. Overall, the results
demonstrate that the proposed multi-stage approach is capable of resolving
business entities across heterogeneous datasets while providing a practical
balance between matching performance and computational efficiency.
