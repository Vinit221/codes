import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

balance_data=pd.read_csv("balance-scale.data",sep=",",header=None)

print("Dataset Length:: ",len(balance_data))
print("Dataset Shape:: ",balance_data.shape)
print(balance_data.head())

X=balance_data.values[:, 1:5]#predicator
Y=balance_data.values[:,0]#target attr (B,R,L)
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.4,random_state=100)

clf_entropy=DecisionTreeClassifier(criterion="entropy",random_state=100,max_depth=3,min_samples_leaf=5)
clf_entropy.fit(X_train,y_train)
clf_gini=DecisionTreeClassifier(criterion="gini",random_state=100,max_depth=3,min_samples_leaf=5)
clf_gini.fit(X_train,y_train)
print(y_test)
y_pred_en=clf_entropy.predict(X_test)
y_pred_gini=clf_gini.predict(X_test)
print(y_pred_en)
print(y_pred_gini)
a=accuracy_score(y_pred_en,y_test)*100
b=accuracy_score(y_pred_gini,y_test)*100
print(a)
print(b)