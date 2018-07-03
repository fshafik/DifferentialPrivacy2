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

n = 100
clf = MLPClassifier(hidden_layer_sizes=(n,n,n),solver='adam',random_state=1,learning_rate_init=0.001,verbose=10,tol=0.000100, max_iter=500)
c = 1;
major_x = pd.DataFrame(columns=['Value'])
major_y = pd.DataFrame(columns=['HH_ID'])

iter_csv = pd.read_csv('H0.csv', iterator=True, chunksize=1000000)
for df in iter_csv:
	df = df[df.Property == 0]
	
	df['Timestamp'] = (((df['Timestamp'] - initial_time)//3600)%24)
	df = df.drop(columns=['ID','Property','H_ID'])

	feature_names = ['Value', 'Timestamp']
	X = df[feature_names]
	feature_names = ['HH_ID']
	y = df[feature_names]

	#y = label_binarize(y, classes=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

	x_train, x_test, y_train, y_test = train_test_split(X, y, test_size= 0.20, random_state=100)

	if c%15==0:
		major_x = pd.concat([major_x,x_test])
		major_y = pd.concat([major_y,y_test])
	else:
		if c == 1:
			all_classes = np.unique(y_train)
			clf.partial_fit(x_train, y_train, classes=all_classes)
		else:
			clf.partial_fit(x_train, y_train)
	c+=1

predictions = clf.predict(major_x)

print('f1 score = ',metrics.f1_score(major_y.HH_ID.values.astype(float),predictions,average='micro'))
print('recall score = ',metrics.recall_score(major_y.HH_ID.values.astype(float),predictions,average='micro'))
print('precision_score = ',metrics.precision_score(major_y.HH_ID.values.astype(float),predictions,average='micro'))
#print('auc _score = ',metrics.roc_auc_score(y_test,predictions,average='micro'))


print('f1 score = ',metrics.f1_score(major_y.HH_ID.values.astype(float),predictions,average='weighted'))
print('recall score = ',metrics.recall_score(major_y.HH_ID.values.astype(float),predictions,average='weighted'))
print('precision_score = ',metrics.precision_score(major_y.HH_ID.values.astype(float),predictions,average='weighted'))