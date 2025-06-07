# Fraud Detection System Using Machine Learning

## Project Overview

In this project, I developed a **Real-Time Fraud Detection System** for digital payment transactions using machine learning techniques. Fraudulent transactions represent a very small fraction of total transactions, making this a challenging imbalanced classification problem. The goal was to build a model that can **accurately detect fraudulent transactions while minimizing false alarms**, thus helping financial institutions reduce losses and protect their customers.

---

## Motivation

- **Rising fraud in digital payments:** As online transactions grow exponentially, fraudsters exploit vulnerabilities, causing financial and reputational damage.
- **Need for automation:** Manual review of transactions is impractical given the volume and speed required.
- **Machine learning advantage:** ML models can learn complex patterns and detect subtle anomalies beyond simple rule-based systems.

---

## Dataset

- The dataset consists of payment transactions labeled as **fraudulent (1)** or **legitimate (0)**.
- Each record includes key features such as:
  - **Transaction amount**
  - **Location** (encoded as categorical data)
  - **Timestamp** (converted to Unix epoch seconds)
- The dataset is highly imbalanced, with a very small percentage of fraudulent cases.

---

## Challenges

- **Severe class imbalance:** Fraud cases are rare, causing the model to be biased towards predicting all transactions as safe.
- **Limited features:** Only a few features were available, making it harder for the model to distinguish fraud.
- **Avoiding false positives:** Over-flagging legitimate transactions can reduce customer trust and increase operational costs.

---

## Solution Approach

### 1. Data Preprocessing

- Categorical features like `location` were encoded as numeric codes.
- Timestamps were converted into Unix epoch time for numeric modeling.
- The dataset was split into training and test sets.

### 2. Handling Imbalanced Data with SMOTE

- **SMOTE (Synthetic Minority Over-sampling Technique)** was used to generate synthetic fraudulent samples in the training set.
- This oversampling balances the class distribution and helps the model learn fraud patterns better.

### 3. Model Selection and Training

- A **Random Forest Classifier** was chosen for its robustness and ability to handle feature interactions.
- The model was trained on the SMOTE-balanced dataset.
- `class_weight='balanced'` was set to further compensate for remaining imbalance.

### 4. Evaluation

- Metrics focused on **precision, recall, and F1-score** rather than accuracy, since accuracy is misleading on imbalanced data.
- The model improved recall of the fraud class from near zero to approximately 17%, meaning it caught more fraud cases.
- Precision was low, indicating some false positives — a common tradeoff in fraud detection.

---

## Results

| Metric      | Legitimate (Class 0) | Fraud (Class 1) |
|-------------|----------------------|-----------------|
| Precision   | 0.99                 | 0.02            |
| Recall      | 0.87                 | 0.17            |
| F1-Score    | 0.93                 | 0.03            |
| Support     | 1977                 | 23              |

- The model successfully identifies a majority of legitimate transactions correctly.
- Fraud detection improved significantly compared to a naive baseline.
- The results highlight the challenges of fraud detection with limited data and imbalanced classes.

---

## Next Steps and Improvements

- **Feature Engineering:** Incorporate more transaction attributes (device ID, merchant category, user behavior patterns).
- **Model Tuning:** Use hyperparameter optimization (GridSearch, RandomSearch) to improve performance.
- **Advanced Algorithms:** Explore gradient boosting models (XGBoost, LightGBM) or deep learning architectures.
- **Threshold Adjustment:** Customize decision thresholds to balance precision and recall based on business needs.
- **Real-time Deployment:** Integrate the model into an API using Flask for live transaction scoring.

---

## Technologies and Tools Used

- Python 3
- Pandas and NumPy for data processing
- Scikit-learn for machine learning modeling
- Imbalanced-learn for SMOTE oversampling
- Joblib for model persistence
- Flask for building a REST API

---

## How to Run the Project

1. Clone the repository
2. Install dependencies:  
3. Prepare your dataset (`your_dataset.csv`) in the project folder.
4. Run the training script:  
5. Start the Flask API server:  
6. Use the provided frontend or API endpoints to make fraud predictions.

---

## Conclusion

This project demonstrates an end-to-end fraud detection pipeline addressing a real-world challenge of imbalanced data. It serves as a foundational step toward building scalable, production-ready fraud prevention systems. The modular structure allows easy integration of new data sources and models for continual improvement.

---

## Contact

If you have any questions or want to collaborate, feel free to reach out!

- Email: devesh090905@gmail.com


---

