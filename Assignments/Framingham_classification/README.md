# Framingham Heart Study — CHD Classification Assignment

## Objective
Predict a patient's **10-year risk of Coronary Heart Disease (CHD)** using health and
lifestyle attributes from the Framingham Heart Study dataset, following a complete
classification ML pipeline.

## Dataset
- **File:** `framingham.csv`
- **Rows:** 4,238 patients
- **Target column:** `TenYearCHD` (0 = No CHD in 10 years, 1 = CHD in 10 years)
- **Features:** demographic (age, sex, education), behavioral (smoking), medical history
  (BP medication, stroke, hypertension, diabetes), and lab measurements (cholesterol,
  blood pressure, BMI, heart rate, glucose).

## Pipeline Summary

| Step | Approach |
|---|---|
| **EDA** | Checked shape, dtypes, missing values, target distribution, correlations, outliers |
| **Missing Values** | Median imputation for continuous columns (`cigsPerDay`, `totChol`, `BMI`, `heartRate`, `glucose`); mode imputation for categorical/binary columns (`education`, `BPMeds`) |
| **Encoding** | Not required — all features were already numeric |
| **Train/Test Split** | 80/20 stratified split (preserves class ratio), done *before* scaling/SMOTE to avoid data leakage |
| **Feature Scaling** | `StandardScaler`, fit on training data only |
| **Class Imbalance** | Dataset is ~85%/15% imbalanced → handled with **SMOTE** on the training set only |
| **Models Trained** | Logistic Regression, KNN, SVM, Decision Tree, Random Forest, Gradient Boosting, AdaBoost, Naive Bayes |
| **Evaluation Metrics** | Accuracy, Precision, Recall, F1-Score, ROC-AUC, Confusion Matrix, Classification Report |
| **Best Model Selection** | Selected by highest F1-Score (balances Precision & Recall — important since missing an at-risk patient is costly) |
| **Hyperparameter Tuning** | `GridSearchCV` with 5-fold CV, optimized for F1-Score |

## Results
- **Best model (by F1-Score, before tuning):** Logistic Regression
- **After GridSearchCV tuning:**
  - Accuracy: 0.664
  - Precision: 0.248
  - Recall: 0.597
  - F1-Score: 0.351
  - ROC-AUC: 0.697

Full metric tables, confusion matrices, and classification reports for all 8 models
are available in the notebook (`Framingham_classification.ipynb`).

## Key Insight
In medical risk prediction, **Recall** on the positive (CHD) class matters more than
raw Accuracy — a False Negative (missing an at-risk patient) is more costly than a
False Positive. The tuned model achieves ~60% recall on the CHD class while keeping
reasonable overall performance.

## Top Predictive Features
Based on Logistic Regression coefficients: **age**, **cigsPerDay**, **male (sex)**,
**sysBP**, and **totChol** were the strongest predictors of 10-year CHD risk.

## Files in this Submission
- `Framingham_classification.ipynb` — full Jupyter notebook (EDA → preprocessing →
  balancing → model training → evaluation → tuning)
- `framingham.csv` — dataset used
- `README.md` — this file

## How to Run
1. Install dependencies: `pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn`
2. Open `Framingham_classification.ipynb` in Jupyter Notebook / JupyterLab / VS Code
3. Run all cells top to bottom
