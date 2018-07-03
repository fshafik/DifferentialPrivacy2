
import numpy as np
import pandas as pd
# import model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# import module to calculate model perfomance metrics
from sklearn import metrics
import matplotlib.pyplot as plt

initial_time = 1378323846
day = 2;

data_path = "HH0_H0.csv"
data = pd.read_csv(data_path, index_col=0)

#df = data[(data.Plug == 2) & (data.Property == 0) & ((data.Timestamp - initial_time)%3600 == 0)]
df = data[(data.Plug == 2) & (data.Property == 1)  & (data.Timestamp > initial_time+((day-1)*3600*24)) & (data.Timestamp <= initial_time+((day)*3600*24))]



feature_names = ['Timestamp']

# use the list to select a subset of the original DataFrame
X = df[feature_names]
# values
y = df.Value

# Splitting X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Linear Regression Model
linreg = LinearRegression()

# fit the model to the training data (learn the coefficients)
linreg.fit(X_train, y_train)

# make predictions on the testing set
y_pred = linreg.predict(X_test)

# The coefficients
print('Coefficients: ', linreg.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % metrics.mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % metrics.r2_score(y_test, y_pred))


# compute the RMSE of our predictions
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)

plt.show()

