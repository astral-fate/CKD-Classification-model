# Kidney Gaurd: CKD classfication



# Project overview

KidneyGaurd is an AI-powered remote self-monitoring solution for kidney health management, utilizing IoT and AI integration.

# Problem

Patients face difficulty detecting kidney diseases early on, often remaining unaware until later stages when dialysis is needed. Additionally, there's a lack of early intervention and collaboration between the health system and patients in the early stages of disease detection.

# Proposed Solution

KidneyGaurd provides real-time prediction of kidney failure stages for kidney patients through blood sample data from remote kidney measurements device. It suggests personalized nutritional recommendations based on patient's biomedical measurements, including Blood Glucose Random, Blood Urea, Serum Creatinine

![Kidney Gaurd](https://github.com/user-attachments/assets/0e7a72aa-d72d-4adf-841b-120a969c84bd)


# Procedures

1. **Data collection:** Users input measurements; Blood Glucose Random, Blood Urea, Serum Creatinine
2. **ML analysis:** ML model processes the input data including
3. **ML Suggestions:** ML predicts the stage of chrnoic kidney disase


# Model Training and Performance

We trained and evaluated several machine learning models to predict kidney disease. Each model was trained on a subset of the data and then evaluated on both validation and test sets. Here's a summary of the models and their performances:

### 1. Random Forest Classifier

The Random Forest model showed exceptional performance:

- **Validation Set Performance:**
  - Accuracy: 98%
  - Balanced performance across classes (0.0 and 1.0)
  - High precision and recall (0.98-0.99) for both classes

- **Test Set Performance:**
  - Accuracy: 99%
  - Consistent high performance, slightly improved from validation

### 2. Support Vector Machine (SVM)

The SVM model showed good performance, with some class imbalance:

- **Validation Set Performance:**
  - Accuracy: 94%
  - Perfect precision for class 1.0, but lower recall (0.79)
  - Very high recall for class 0.0 (1.00), with good precision (0.93)

### 3. Decision Tree

The Decision Tree model performed well, nearly matching Random Forest:

- **Validation Set Performance:**
  - Accuracy: 98%
  - Balanced performance across classes
  - High precision and recall (0.95-0.99) for both classes

### 4. Logistic Regression

Logistic Regression showed strong performance:

- **Validation Set Performance:**
  - Accuracy: 97%
  - Slightly better precision for class 1.0 (0.98) than class 0.0 (0.97)
  - Higher recall for class 0.0 (0.99) than class 1.0 (0.91)

### Model Comparison

1. **Random Forest** emerged as the top performer, with the highest accuracy and balanced performance across classes in both validation and test sets.
2. **Decision Tree** closely followed Random Forest in performance.
3. **Logistic Regression** showed strong results, with slight variations in class-specific metrics.
4. **SVM** demonstrated good overall accuracy but showed some class imbalance in its predictions.

Based on these results, the **Random Forest** model was selected as the primary model for our kidney disease prediction system due to its superior and consistent performance across both validation and test datasets.


## Evaluation Metrics

- Feature Importance
![image](https://github.com/user-attachments/assets/954e203b-23c5-4841-9e11-7bd5c4699ad1)




## Results

- Generated synthetic dataset of size 5K for binary chrnoic kidney disase classfication
- Utlized 4 diffrent Machine learning model to predict stages of chrnoic kidney disases
- Achived result of 98% accuracy using Random Forest on validation dataset
- Deployed ML pipeline model with Flask and PythonAnyWhere


## Confusion Matrix


![image](https://github.com/user-attachments/assets/e522802a-1da3-46cb-a9d3-a9fe9a72ab6e)



## Classification Report (Validation Set)

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| -0.0  | 0.99      | 0.99   | 0.99     | 741     |
| 1.0   | 0.98      | 0.97   | 0.97     | 259     |

| Metric       | Precision | Recall | F1-Score | Support |
|--------------|-----------|--------|----------|---------|
| Accuracy     |           |        | 0.98     | 1000    |
| Macro Avg    | 0.98      | 0.98   | 0.98     | 1000    |
| Weighted Avg | 0.98      | 0.98   | 0.98     | 1000    |

This classification report demonstrates:
- Exceptional performance for both classes (-0.0 and 1.0)
- High precision and recall across the board
- An overall accuracy of 98%

The Random Forest model shows balanced performance between the two classes, indicating its effectiveness in identifying both positive and negative cases of kidney disease with high reliability.

# Model Deployment

![Kidney Gaurd (1)](https://github.com/user-attachments/assets/ee6f6f19-dab7-494b-b0de-3a48366a4a18)




