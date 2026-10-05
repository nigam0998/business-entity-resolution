# Business Entity Resolution

> A multi-stage machine learning pipeline for resolving business entities across heterogeneous datasets.

## 👥 Authors

| Author | Role |
|---|---|
| **Devyansh Nigam** | Lead Developer & ML Engineer |
| **Sejal Saquib** | Data & Research Analyst |

---

## 📌 Project Overview

Business entity resolution is the task of determining whether records from different datasets refer to the same real-world business.

This project implements a multi-stage entity-resolution pipeline combining candidate generation, blocking techniques, similarity features, exact-name matching, and supervised machine learning.

## 🎯 Objectives

- Identify potential matches between business records.
- Reduce comparisons through candidate generation.
- Combine multiple blocking strategies.
- Engineer name, address, and country similarity features.
- Train a supervised classification model.
- Optimize the classification threshold.
- Analyze false positives, false negatives, and missing candidates.
- Evaluate the complete entity-resolution pipeline.

## 🏗️ System Architecture

```text
Business Records
       ↓
Data Preprocessing
       ↓
Candidate Generation
       ↓
┌──────────────┬──────────────┬──────────────┐
│ Token Block  │ Address Block│ Exact Name   │
└──────────────┴──────────────┴──────────────┘
       ↓
Candidate Union
       ↓
Feature Engineering
       ↓
Logistic Regression
       ↓
Probability Scores
       ↓
Threshold Optimization
       ↓
Final Matches
```

## 🔍 Candidate Generation

Candidate generation reduces the number of source-target comparisons.

### Token-based Blocking

Business names and addresses are tokenized and indexed to retrieve potentially matching records.

### Address-based Blocking

Address tokens are used to identify records that may refer to the same location.

### Exact-name Blocking

An exact normalized business-name index is used to recover candidates missed by token-based blocking.

### Candidate Union

Candidates from multiple blocking strategies are combined before ranking and classification.

## 🧮 Feature Engineering

The model uses multiple similarity and matching features:

- Name similarity ratio
- Name token similarity
- Address similarity ratio
- Address token similarity
- Name Jaccard similarity
- Address Jaccard similarity
- Country match
- Exact-name match
- Shared-token information
- Candidate rank

## 🤖 Machine Learning Model

The final classifier is Logistic Regression implemented using scikit-learn.

```python
LogisticRegression(
    class_weight="balanced",
    max_iter=1000,
    random_state=42
)
```

A StandardScaler is applied before Logistic Regression. Balanced class weights are used because of the strong class imbalance.

## 📊 Dataset Split

| Dataset | Pairs | Positive | Negative |
|---|---:|---:|---:|
| Training | 71,092 | 999 | 70,093 |
| Validation | 17,364 | 242 | 17,122 |
| Test | 17,364 | 242 | 17,122 |

## 📈 Final Model Results

The selected classification threshold was **0.95**.

| Metric | Score |
|---|---:|
| Accuracy | **99.35%** |
| Precision | **73.55%** |
| Recall | **83.88%** |
| F1-score | **78.38%** |
| Decision threshold | **0.95** |

### Confusion Matrix

```text
                 Predicted
                Negative Positive
Actual Negative   17049      73
Actual Positive      39     203
```

## 🔎 Candidate Generation Results

Candidate generation was evaluated on **500 source entities**.

| Metric | Result |
|---|---:|
| Sources evaluated | 500 |
| Gold matches | 1,778 |
| Retrieved gold matches | 1,398 |
| Candidate recall | **78.63%** |
| Average final candidates/source | 500.86 |
| Maximum final candidates/source | 2,363 |

Candidate recall is separate from classifier recall. A genuine pair excluded during candidate generation cannot be recovered by the downstream classifier.

## 🎚️ Threshold Analysis

The best observed F1-score occurred at threshold **0.95**:

- Precision: **73.55%**
- Recall: **83.88%**
- F1-score: **78.38%**

## 🧪 Error & Missing-Candidate Analysis

The analysis identified:

- **496** missing genuine candidate pairs
- **328** missing pairs with zero generated candidates
- **168** missing pairs where candidates existed but the genuine target was absent

Exact-name blocking recovered **85** of the 328 zero-candidate cases, giving an exact-name recovery rate of **25.91%**.

## 📁 Repository Structure

```text
business-entity-resolution/
│
├── output/
│   ├── candidate_recall.png
│   ├── candidate_recall_results.csv
│   ├── confusion_matrix.png
│   ├── final_model_results.csv
│   ├── threshold_comparison.png
│   └── FINAL_REPORT.md
│
├── README.md
└── project source / notebooks
```

## 📊 Generated Outputs

| File | Description |
|---|---|
| `candidate_recall.png` | Candidate-generation performance |
| `candidate_recall_results.csv` | Candidate-generation evaluation |
| `confusion_matrix.png` | Final classification confusion matrix |
| `final_model_results.csv` | Final model metrics |
| `threshold_comparison.png` | Threshold performance comparison |
| `FINAL_REPORT.md` | Detailed written project report |

## 🛠️ Technology Stack

- Python
- Pandas
- NumPy
- scikit-learn
- Google Colab
- Git
- GitHub

## ⚠️ Limitations

The primary limitation is candidate-generation recall. The final candidate-generation recall was **78.63%**, meaning some genuine matches were excluded before classification.

The dataset also contains substantial class imbalance, addressed using balanced class weights.

## 🚀 Future Improvements

- More advanced blocking strategies
- Phonetic name matching
- Character-level similarity
- Geographic similarity
- Better abbreviation handling
- Semantic and embedding-based similarity
- Transformer-based entity matching
- Learning-to-rank models
- Improved recovery of missing candidate pairs
- Larger and more diverse evaluation datasets

## 📌 Key Findings

1. Multiple blocking strategies provide complementary candidate coverage.
2. Exact-name indexing can recover cases missed by token-based candidate generation.
3. Candidate generation is the main bottleneck because missing candidates cannot be recovered downstream.
4. The Logistic Regression classifier achieves a strong precision-recall balance at threshold 0.95.
5. The final classifier achieves an F1-score of **78.38%**.

## 📄 Project Report

The detailed report is available at `output/FINAL_REPORT.md`.

## 👨‍💻 Authors

### Devyansh Nigam
**Lead Developer & ML Engineer**

Contributions:
- Pipeline implementation
- Candidate generation and blocking
- Feature engineering
- Machine learning model development
- Threshold optimization
- Model evaluation
- Git/GitHub integration

### Sejal Saquib
**Data & Research Analyst**

Contributions:
- Data analysis
- Entity-resolution research
- Evaluation and error analysis
- Experimental-result interpretation
- Project documentation

## 📜 Status

**Project Status: Completed**

The candidate-generation pipeline, machine-learning model, evaluation, error analysis, result artifacts, and final project report have been completed.
