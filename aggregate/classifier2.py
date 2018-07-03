from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn import metrics
from sklearn.preprocessing import label_binarize
import numpy as np
import pandas as pd
import array
import random
import itertools
# digits = datasets.load_digits()
# images = digits.images
# targets = digits.target

initial_time = 1378323846

NN = 16
NL = 16
NS = 16
Lambda =1e-03
BS = 64
ir = 0.001
pt = 0.5

clf = MLPClassifier(
	 hidden_layer_sizes=(NN,NL,NS),
	 solver='adam',alpha=Lambda,batch_size=BS,beta_1=0.9,beta_2=0.999,
	 learning_rate='adaptive',learning_rate_init=ir,power_t=pt,max_iter=20,
	 shuffle=True,random_state=1,tol=0.0001,early_stopping=True,verbose=True)	

c = 1;

iter_csv = pd.read_csv('housedata.csv', iterator=True, chunksize=1000000)
temp = iter_csv.get_chunk(10000000)
#print(temp)
temp['timestamp'] = (((temp['timestamp'] - initial_time)//3600)%24)//6

X = temp[['agg','timestamp']]
Y = temp[['HH']]
Y = label_binarize(Y, classes=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
#Y = temp[['class0','class3','class1','class2','class6','class7','class8','class9','class11','class4','class5', 'class10', 'class12', 'class13']]
# X = preprocessing.normalize(X,axis=0)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=100)
#combine = [X_train,Y_train]

scaler = StandardScaler()
scaler.fit(X_train)


X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


clf.fit(X_train,Y_train)

	

predictions = clf.predict(X_test)
print('f1 score = ',metrics.f1_score(Y_test,predictions,average='micro'))
print('recall score = ',metrics.recall_score(Y_test,predictions,average='micro'))
print('precision_score = ',metrics.precision_score(Y_test,predictions,average='micro'))
print('auc _score = ',metrics.roc_auc_score(Y_test,predictions,average='micro'))
