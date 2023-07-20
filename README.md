# Linear Regression from Scratch

This repository contains an implementation of Linear Regression from scratch in Python without using any external machine learning libraries. Linear Regression is a fundamental machine learning algorithm used for predicting continuous numeric values based on input features. The project explores the concepts of data preprocessing, model training, and evaluation for linear regression.

## Project Overview

- **Data Preprocessing:** The project includes data preprocessing techniques, such as loading data from CSV files, handling missing values, and normalizing the data to improve model performance.

- **Linear Regression Implementation:** The core implementation of Linear Regression is done from scratch, without using any machine learning libraries. The project includes functions for calculating model parameters and making predictions.

- **Data Visualization:** Data exploration and visualization techniques are used to gain insights into the dataset and understand the relationship between the features and target variable.

- **Model Evaluation:** The project evaluates the performance of the Linear Regression model using metrics like mean squared error (MSE) and coefficient of determination (R-squared).

## File Structure

- `linear_regression.py`: Python script containing the implementation of Linear Regression and related functions.

- `dataset/train.csv`: Sample training dataset in CSV format used for training the Linear Regression model.

- `dataset/test.csv`: Sample test dataset in CSV format used for evaluating the model.
- `data_normalization.py` : Min-max method for data normalization.
- `data_visualization.py` : Visuazliation of given points with matplotlib.
- `data_load.py` : Loading data into arrays.

## Getting Started

1. **Clone the repository:** `git clone https://github.com/yourusername/linear-regression-from-scratch.git`

2. **Install Python and required libraries:** The project uses standard Python libraries like pandas and matplotlib. Make sure you have them installed.

3. **Run the script:** Navigate to the project directory and execute `python linear_regression.py` to train the model and evaluate its performance.

## Results

The Linear Regression model is trained on the provided training dataset and evaluated on the test dataset. The model's performance is reported in terms of the mean squared error (MSE) and R-squared values. You can modify the `train.csv` and `test.csv` files with your own datasets to explore and experiment with different data.

**Note:**
This project is intended for educational purposes to understand the fundamentals of Linear Regression and its implementation from scratch. For real-world applications, it is recommended to use established machine learning libraries like scikit-learn for more efficient and optimized implementations.
