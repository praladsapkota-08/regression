# Credit Card Fraud Detection

## Overview
This project detects credit card fraud using machine learning, focusing on an imbalanced dataset from Kaggle. The best model, XGBoost with SMOTE (`xgb_class_smote`), achieves an AUPRC of 0.8832, precision of 0.85, and recall of 0.84. The project includes a Streamlit app for real-time predictions.

## Dataset
- Source: [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data) (Kaggle)
- License: CC0 1.0 Universal (Public Domain)
- Description: 284,807 transactions, 0.17% fraudulent, with PCA-transformed features (`V1`-`V28`), `Time`, and `Amount`.

## Installation
### Pip
```bash
pip install -r requirements.txt