# Flipkart Customer Satisfaction Prediction and AI Recommendation System

## Overview

This project focuses on predicting customer satisfaction for an e-commerce platform using Machine Learning techniques and integrating a Generative AI recommendation system for business insights.

Customer satisfaction plays a major role in improving customer retention and business growth in online shopping platforms. Large amounts of customer feedback and customer-related information make manual analysis difficult and time-consuming.

This project automates the process by:

* Predicting whether a customer is **Satisfied** or **Unsatisfied**
* Analyzing customer remarks
* Generating AI-powered recommendations
* Providing an interactive deployment application

The final system combines **Machine Learning + Generative AI + Streamlit deployment** to provide an end-to-end solution.

---

## Problem Statement

E-commerce platforms receive large volumes of customer feedback every day. Identifying dissatisfied customers manually is difficult and can lead to delayed actions and poor customer retention.

The main objective of this project is to build an intelligent system that can:

* Predict customer satisfaction status
* Analyze customer feedback
* Generate meaningful recommendations
* Assist businesses in decision-making

---

## Project Objectives

The objectives of this project are:

* Perform Exploratory Data Analysis (EDA)
* Clean and preprocess customer data
* Handle missing values and duplicates
* Apply text preprocessing techniques
* Handle class imbalance
* Train multiple machine learning models
* Perform hyperparameter optimization
* Compare model performance
* Select the best-performing model
* Integrate Generative AI recommendations
* Deploy the project as an interactive application

---

## Dataset Description

The dataset contains customer-related information and feedback collected from Flipkart customer records.

### Dataset Features

Examples of features used:

* Customer Age
* Order Priority
* Customer Remarks
* Product Information
* Delivery Details
* Customer Ratings
* Other customer-related variables

### Target Variable

**Satisfaction_Category**

Classes:

* Satisfied
* Unsatisfied

---

## Project Workflow

```text
Data Collection
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Text Preprocessing
        ↓
Feature Engineering
        ↓
TF-IDF Vectorization
        ↓
Dimensionality Reduction
        ↓
Train-Test Split
        ↓
SMOTE for imbalance handling
        ↓
Model Building
        ↓
Cross Validation
        ↓
Hyperparameter Tuning
        ↓
Final Model Selection
        ↓
Generative AI Integration
        ↓
Deployment using Streamlit
```

---

## Exploratory Data Analysis

Exploratory Data Analysis was performed to understand:

* Distribution of customer satisfaction
* Missing values
* Duplicate records
* Feature relationships
* Class imbalance
* Text data characteristics

Visualizations used:

* Count plots
* Histograms
* Correlation heatmaps
* Box plots
* Distribution plots

---

## Data Preprocessing

The following preprocessing techniques were applied:

### Data Cleaning

* Missing value treatment
* Duplicate removal
* Data type conversion

### Text Preprocessing

Customer remarks were processed using:

* Lowercasing
* Tokenization
* Stopword removal
* Lemmatization
* Part-of-Speech tagging
* TF-IDF Vectorization

### Dimensionality Reduction

Dimensionality reduction was performed after TF-IDF to reduce feature complexity and improve computational efficiency.

---

## Train-Test Split

The dataset was split into:

* Training Data: 80%
* Testing Data: 20%

---

## Handling Imbalanced Dataset

The target variable showed class imbalance:

Before SMOTE:

```text
Satisfied      86%
Unsatisfied    14%
```

SMOTE (Synthetic Minority Oversampling Technique) was used to balance the classes.

After SMOTE:

```text
Satisfied      36948
Unsatisfied    36948
```

Benefits:

* Reduces model bias
* Improves minority class prediction
* Improves Recall and F1 Score

---

## Machine Learning Models Used

Three machine learning models were implemented and compared:

### 1. Logistic Regression

* Linear classification algorithm
* Simple and interpretable

### 2. Random Forest

* Ensemble learning technique
* Uses multiple decision trees
* Reduces overfitting
* Provides feature importance

### 3. XGBoost

* Gradient boosting algorithm
* Optimized for performance and speed

---

## Cross Validation

Cross Validation was applied to evaluate model stability and reduce overfitting.

Technique used:

* K-Fold Cross Validation

Benefits:

* Better generalization
* Reliable model evaluation

---

## Hyperparameter Optimization

GridSearchCV was used for hyperparameter optimization.

Parameters tuned included:

* Number of estimators
* Maximum depth
* Learning rate
* Regularization parameters

Benefits:

* Improves model performance
* Finds optimal parameter combinations

---

## Final Model Selection

Final selected model:

**Random Forest Classifier**

Random Forest was selected because:

* Stable performance
* Better generalization
* Reduced overfitting
* Provides feature importance analysis

---

## Model Performance

Evaluation metrics used:

* Accuracy
* Precision
* Recall
* F1 Score

### Final Metrics

Update with your actual values:

```text
Accuracy : 84%

Precision : 88%

Recall : 62%

F1 Score : 73%
```

---

## Business Impact of Evaluation Metrics

### Accuracy

Shows overall prediction correctness.

Business impact:

* Helps evaluate overall system reliability.

### Precision

Measures prediction correctness for positive predictions.

Business impact:

* Reduces incorrect customer targeting.

### Recall

Measures the ability to identify dissatisfied customers.

Business impact:

* Helps identify unhappy customers early.

### F1 Score

Balances Precision and Recall.

Business impact:

* Provides balanced model performance.

---

## Generative AI Integration

Generative AI was integrated to generate business recommendations after prediction.

Workflow:

```text
Customer Input
        ↓
Machine Learning Prediction
        ↓
Customer Remark Analysis
        ↓
AI Recommendation Generation
        ↓
Business Insight
```

Example:

Customer Remark:

```text
Delivery was delayed and support response was slow
```

Prediction:

```text
Unsatisfied
```

AI Recommendation:

```text
Customer dissatisfaction appears related to delayed delivery and customer support issues.

Recommended Actions:

• Improve delivery tracking
• Improve support response time
• Prioritize complaint handling
```

---

## Deployment

The project was deployed using Streamlit.

Run locally:

```bash
streamlit run app/app.py
```
---

## Future Improvements

Potential future enhancements include:

* Real-time prediction system
* Azure cloud deployment
* LLM integration
* Chatbot functionality
* Personalized customer recommendations
* Real-time feedback analysis

---

## Conclusion

This project successfully combined Machine Learning and Generative AI techniques to predict customer satisfaction and generate actionable business insights. The system can help businesses understand customer behavior, improve customer experience, and support better decision-making.

---


