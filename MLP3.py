import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt

from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.preprocessing import label_binarize

initial_time = 1378323846
day = 1;

n = 100
clf = MLPRegressor(hidden_layer_sizes=(n,n,n),solver='adam',random_state=1,learning_rate_init=0.001,verbose=10,tol=0.000100, max_iter=500)

c = 1;
major_x = pd.DataFrame(columns=['HH_ID'])
major_y = pd.DataFrame(columns=['Value'])


iter_csv = pd.read_csv('H0.csv', iterator=True, chunksize=1000000)
df = iter_csv.get_chunk(100000)
df = df[df.Property == 0]
	
df = df.drop(columns=['ID','Property','H_ID'])

feature_names = ['HH_ID']
X = df[feature_names]
feature_names = ['Value']
y = df[feature_names]
	

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size= 0.20, random_state=100)

#	if c%15==0:
#		major_x = pd.concat([major_x,x_test])
#		major_y = pd.concat([major_y,y_test])
#	else:
#		clf.partial_fit(x_train, y_train)
#	c+=1
clf.fit(x_train, y_train)
predictions = clf.predict(x_test)

#print('f1 score = ',metrics.f1_score(major_y.Value.values.astype(float),predictions,average='micro'))
#print('recall score = ',metrics.recall_score(major_y.Value.values.astype(float),predictions,average='micro'))
#print('precision_score = ',metrics.precision_score(major_y.Value.values.astype(float),predictions,average='micro'))

print("Mean squared error: %.2f" % metrics.mean_squared_error(y_test, predictions))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % metrics.r2_score(y_test, predictions))
