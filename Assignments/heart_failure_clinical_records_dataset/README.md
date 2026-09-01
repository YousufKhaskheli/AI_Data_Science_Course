# Heart Failure Clinical Records — Death Event Classification Assignment

## Objective
Predict whether a patient with heart failure will experience a **death event**
(`DEATH_EVENT`) during the follow-up period, using clinical and lab-measurement
attributes from the Heart Failure Clinical Records dataset, following a complete
classification ML pipeline.

## Dataset
- **File:** `heart_failure_clinical_records_dataset.csv`
- **Rows:** 299 patients
- **Target column:** `DEATH_EVENT` (0 = survived follow-up, 1 = death during follow-up)
- **Features:** demographic (age, sex), lifestyle (smoking), medical history (anaemia,
  diabetes, high blood pressure), and lab measurements (creatinine phosphokinase,
  ejection fraction, platelets, serum creatinine, serum sodium), plus `time`
  (follow-up period length in days).

## Pipeline Summary

| Step | Approach |
|---|---|
| **EDA** | Checked shape, dtypes, missing values, target distribution, correlations, outliers |
| **Missing Values** | None found in the dataset — a general-purpose median/mode imputation step is still included for reusability, but has nothing to do |
| **Encoding** | Not required — all features were already numeric |
| **Train/Test Split** | 80/20 stratified split (preserves class ratio), done *before* scaling/balancing to avoid data leakage |
| **Feature Scaling** | `StandardScaler`, fit on training data only |
| **Class Imbalance** | Dataset is ~68%/32% imbalanced → handled with a **SMOTE** (k-NN based oversampling) implementation on the training set only |
| **Models Trained** | Logistic Regression, KNN, SVM, Decision Tree, Random Forest, Gradient Boosting, AdaBoost, Naive Bayes |
| **Evaluation Metrics** | Accuracy, Precision, Recall, F1-Score, ROC-AUC, Confusion Matrix, Classification Report |
| **Best Model Selection** | Selected by highest F1-Score (balances Precision & Recall — important since missing a patient at risk of death is costly) |
| **Hyperparameter Tuning** | `GridSearchCV` with 5-fold CV, optimized for F1-Score |

## Results
- **Best model (by F1-Score, before tuning):** Decision Tree (Accuracy 0.833, Precision 0.765, Recall 0.684, F1-Score 0.722, ROC-AUC 0.793)
- **After GridSearchCV tuning** (`criterion='entropy'`, `max_depth=7`, `min_samples_split=2`; best 5-fold CV F1-Score = 0.855):
  - Accuracy: 0.783
  - Precision: 0.667
  - Recall: 0.632
  - F1-Score: 0.649
  - ROC-AUC: 0.758

  Note: the tuned model scored higher on cross-validation (0.855 F1) than the untuned
  model, but slightly lower on the small held-out test set (60 patients). With such a
  small dataset, the test split carries meaningful variance — this is discussed directly
  in the notebook rather than hidden.

Full metric tables, confusion matrices, and classification reports for all 8 models are
available in the notebook (`Heart_Failure_Classification.ipynb`).

## Key Insight
In medical risk prediction, **Recall** on the positive (Death) class matters as much as
raw Accuracy — a False Negative (predicting a patient will survive when they actually die)
is more costly than a False Positive. The dataset's imbalance (~68% survived / ~32% death)
was corrected with SMOTE before training so models don't simply default to predicting the
majority "survived" class.

## Top Predictive Features
Based on the tuned Decision Tree's feature importances: **time** (length of the follow-up
period), **ejection_fraction**, **serum_creatinine**, **platelets**, and
**creatinine_phosphokinase** were the strongest predictors of a death event. `sex` had
effectively no predictive value.

## Files in this Submission
- `Heart_Failure_Classification.ipynb` — full Jupyter notebook (EDA → preprocessing →
  balancing → model training → evaluation → tuning)
- `heart_failure_clinical_records_dataset.csv` — dataset used
- `README.md` — this file

## How to Run
1. Install dependencies: `pip install pandas numpy matplotlib seaborn scikit-learn`
   (the notebook includes its own dependency-free SMOTE implementation, so
   `imbalanced-learn` is optional — if it's installed, `from imblearn.over_sampling
   import SMOTE` can be swapped in as a drop-in replacement)
2. Open `Heart_Failure_Classification.ipynb` in Jupyter Notebook / JupyterLab / VS Code
3. Run all cells top to bottom
