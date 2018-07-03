from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn import metrics
import pandas
import array
import random
# digits = datasets.load_digits()
# images = digits.images
# targets = digits.target

temp = pandas.read_csv("../noiseaddition/DP-finaldata2.csv")
temp = temp[temp['timestamp']%2 == 0]
X = temp[['agg']]
#Y = temp[['HH']]
Y = temp[['class0','class3','class1','class2','class6','class7','class8','class9','class11','class4','class5']]
# X = preprocessing.normalize(X,axis=0)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=100)

#combine = [X_train,Y_train]

scaler = StandardScaler()
scaler.fit(X_train)


X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

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


clf.fit(X_train,Y_train)

predictions = clf.predict(X_test)
print('f1 score = ',metrics.f1_score(Y_test,predictions,average='micro'))
print('recall score = ',metrics.recall_score(Y_test,predictions,average='micro'))
print('precision_score = ',metrics.precision_score(Y_test,predictions,average='micro'))
print('auc _score = ',metrics.roc_auc_score(Y_test,predictions,average='micro'))
# print('classification_report _score = ',metrics.classification_report(Y_test,predictions,average='micro'))

# print('roc score = ',metrics.roc_curve(Y_test,predictions,average='samples'))
# print(metrics.mean_squared_error(Y_test,predictions),metrics.mean_absolute_error(Y_test,predictions))
