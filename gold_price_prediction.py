# -*- coding: utf-8 -*-
"""Gold Price Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VDrISZiq8g8MmBNGzBNVqsk2dLtPe0qK

Importing Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

"""Collecting data and processing

"""

#loading csv data into pandas dataframe
gold_data = pd.read_csv('/content/gld_price_data.csv')

#printing five rows
gold_data.head()

gold_data.tail()

#checking the numbers of rows and columns
gold_data.shape

#getting info about the data we are dealing with
gold_data.info()

#checking the number of missng values
gold_data.isnull().sum()

#getting the statistical measures of data
gold_data.describe()

"""Checking the correlation between values

"""

# Convert the 'date' column to datetime
gold_data['Date'] = pd.to_datetime(gold_data['Date'])

# Exclude the 'date' column when calculating correlation
correlation = gold_data.select_dtypes(include=[float, int]).corr()

#understanding the data
plt.figure(figsize=(8, 8))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size': 8}, cmap='YlGnBu')
plt.show()

#correlation values of GLD
print(correlation['GLD'])

#checking the distribution of the gold price
sns.displot(gold_data["GLD"], color='green')

#Splitting the features and target
X = gold_data.drop(['Date', 'GLD'], axis=1)
Y = gold_data['GLD']

print(Y)

"""Splitting into training data and test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state=2)

"""Random Forest Algorithm

single decision tree
"""

regressor = RandomForestRegressor(n_estimators=100)

#training the model
regressor.fit(X_train, Y_train)

"""Evaluating our model based on test data and train data"""

#prediction
test_data_predicted = regressor.predict(X_test)

#R squared error
error_score = metrics.r2_score(Y_test, test_data_predicted)
print("R squared error is :", error_score)

"""Comparision using plots"""

Y_test = list(Y_test)

plt.figure(figsize=(14, 8))  # Larger figure size
plt.plot(Y_test, color='orange', label='Actual Value', linewidth=3, linestyle='-', marker='o')  # Change to orange
plt.plot(test_data_predicted, color='purple', label='Predicted Value', linewidth=3, linestyle='--', marker='x')  # Change to purple
plt.title('Actual Price vs Predicted Price', fontsize=18, fontweight='bold')  # Larger and bold title
plt.xlabel('Number of Values', fontsize=14)  # Larger x-axis label
plt.ylabel('GLD Price', fontsize=14)  # Larger y-axis label
plt.legend(loc='best', fontsize=14)  # Larger legend
plt.grid(True, which='both', linestyle='--', linewidth=0.7)  # Thinner grid for clarity
plt.tight_layout()  # Adjust layout for better spacing
plt.show()

