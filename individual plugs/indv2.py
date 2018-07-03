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

df = pd.read_csv('indv_hour22.csv')


#df['min'] = ((df['min']/60)%24)//6
feature_names = ['value']

#df['hour'] = ((df['hour'])%24)
#feature_names = ['value', 'hour']

X = df[feature_names]
#print(X)
#y = np.asarray(df['Value'], dtype="|S6")
y = df.plug
y = label_binarize(y, classes=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11])
#print(y)


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

