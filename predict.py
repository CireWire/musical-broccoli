'''
AMZN Stock Price Prediction using Linear Regression
Author: Eric Gutierrez Jr.
Date: 04/28/2023
Description: This program uses Linear Regression to predict the stock price of Amazon (AMZN) for the next 30 days.
License: MIT License
predict.py

'''
# /usr/bin/python3

# Import the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Read the data
data = pd.read_csv('AMZN.csv')
data = data[['Close']]

# Predict 'n' days into the future
future_days = 30
data['Prediction'] = data[['Close']].shift(-future_days)

# Create the feature data set (X) and convert it to a numpy array
X = np.array(data.drop(['Prediction'], axis=1))[:-future_days]

# Create the target data set (y) and convert it to a numpy array
y = np.array(data['Prediction'])[:-future_days]

# Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the model
model = LinearRegression()
model.fit(x_train, y_train)

# Test the model using score which returns the coefficient of determination R^2 of the prediction
lr_confidence = model.score(x_test, y_test)
print("lr confidence: ", lr_confidence)

# Get the last 'n' rows of the feature data set
x_future = data.drop(['Prediction'], axis=1)[:-future_days]

# Print the predictions for the next 'n' days
lr_prediction = model.predict(x_future)
print(lr_prediction)