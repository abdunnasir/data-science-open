# Predict salary based on year

# Importing the libraries
import pandas as pd
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# from flask import jsonify

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Persist python objects into the files, so that they can be read from the api.
joblib.dump(regressor, 'model.pkl')
joblib.dump(dataset, 'dataset.pkl')

print ('perfect')
