
# Module 5 Final Project



## Executive Summary

The goal of project is to use different classification models to analyze a medical dataset in order to predict the presence or absence of cardiovascular disease using examination results in patients.


## Introduction

The dataset was sourced from Kaggle.  The dataset originally contained 70,000 patient records consisting of 11 features (5 continuous and 6 categorical).  After the data was cleaned, the outlying points deleted and an additional continuous feature added, Body Mass Index, the working dataset was just shy of 69,000 patient records. A target equal to 1 indicated that a patient suffered from heart disease and a 0 meant they did not.

## Approach

The data was downloaded from Kaggle and cleaned.  After creating visualizations to get a deeper understanding of the data, an additional feature, Body Mass Index, was engineered.  Classification was done in two stages. In the first stage, the classification models used were:
1. Logistic Regression (Log Reg)
2. Random Forest (RF)
3. K-Nearest Neighbor (KNN)
4. Support Vector Machine (SVM)

In the second stage, Principal Component Analysis (PCA) was employed.  It was determined that the optimal n_components to use was 10 and for additional insight a value of n_components equal to 2 was used.  The models in the second stage of classification were:
1. SVM 
2. SVM with n_components =2 and =10
3. Log Reg 
4. Log Reg with n_components =2 and =10
5. KNN with n_components =2 and =10

The accuracy and precision metrics were used to compare the models' performance.


## Libraries

- the usual: numpy and pandas
- seaborn and matplotlib for plotting
- scikit.learn classification models such as Logistic Regression, Random Forest, Support Vector Matrix and KNN
- scikit.learn metrics, confusion matrices and classification reports
- skikit.learn PCA 
- time
- scikit.learn StandardScaler() and train_test_split


## Files

The applicable files in this repository for the user are on this project are:

- cardio_train.csv is the data set used in this analysis and contains 
- README.md is this file.
- student.ipynb is the jupyter notebook containing the analysis and modeling
- my_helper_functions.py was my attempt to keep helper functions out of the jupyter notebook, this was unsuccessful despite numerous attempts.

## Results and Conclusion

The accuracy metric was used to compare the models, as well as, the precision and recall metric. For accuracy, the SVM classification model performed the best followed closely in second place by the SVM model with n_components =10. For precision, the SVM model still outperformed the others. However, in recall performance, the best model was the SVM model with n_components=2. Although it is not a clear cut case, the evidence leads to the conclusion that the best performing model in this classification report is the SVM. The confusion matrix for the SVM model:
0 | 6620 | 1814|
1 | 2737 | 5784|
  |  0   |  1  |
  
TP = 6620, FN = 1814
FP = 2737, TN = 5784

The accuracy, precision and recall of the SVM is: 73.47%, 76.13% and 66.64%.

