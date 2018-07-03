import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.preprocessing import label_binarize

initial_time = 1378323846
day = 1;

df = pd.read_csv('HH0_H0.csv')

#df = df[(df.Property == 1) & (df.Timestamp > initial_time+((day-1)*3600*24)) & (df.Timestamp <= initial_time+((day+7)*3600*24))]
#df = df[(df.Property == 1) & ((df.Timestamp-initial_time)%60 == 0)] 
df = df[(df.Property == 0) & ((df.Timestamp-initial_time)%(10) == 0)] 

df['Timestamp'] = (((df['Timestamp'] - initial_time)//3600)%24)//12
df = df.drop(columns=['ID','Property','HH_ID','H_ID'])

feature_names = ['Value', 'Timestamp']

X = df[feature_names]
y = df.Plug
y = label_binarize(y, classes=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size= 0.20, random_state=100)

scaler = StandardScaler()
scaler.fit(x_train)


x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

n = 100

clf = MLPClassifier(hidden_layer_sizes=(n,n,n,n,n),solver='adam',random_state=1,learning_rate_init=0.001,verbose=10,tol=0.0000100, max_iter=500)

clf.fit(x_train, y_train)

predictions = clf.predict(x_test)
print('f1 score = ',metrics.f1_score(y_test,predictions,average='micro'))
print('recall score = ',metrics.recall_score(y_test,predictions,average='micro'))
print('precision_score = ',metrics.precision_score(y_test,predictions,average='micro'))
print('auc _score = ',metrics.roc_auc_score(y_test,predictions,average='micro'))

