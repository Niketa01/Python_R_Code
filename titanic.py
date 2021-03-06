# -*- coding: utf-8 -*-
"""titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dZVkY0hf4YYneMSZjocakwtSDcdNQ3os
"""

import pandas as pd
df=pd.read_csv(r'/content/train.csv')
df.head()

df=df[['PassengerId','Pclass','Sex','Age','SibSp','Parch','Fare','Survived']]
df.Sex[df.Sex=='male']=1
df.Sex[df.Sex=='female']=2
df.head()

x=df.iloc[:,0:7]
y=df.iloc[:,7]
x.head()

df1=pd.read_csv(r'/content/test.csv')
df1=df1[['PassengerId','Pclass','Sex','Age','SibSp','Parch','Fare']]
df1.Sex[df1.Sex=='male']=1
df1.Sex[df1.Sex=='female']=2
df1.head()

pd.isna(x).sum()

from sklearn.impute import KNNImputer
imp=KNNImputer(n_neighbors=2, weights="uniform")
x_new=pd.DataFrame(imp.fit_transform(x), columns=x.columns)
print(x_new)
pd.isna(x_new).sum()

test=pd.DataFrame(imp.fit_transform(df1), columns=df1.columns)
print(test)
pd.isna(test).sum()

from sklearn.tree import DecisionTreeClassifier
cl=DecisionTreeClassifier()
cl=cl.fit(x_new,y)
y_pred=cl.predict(test)
y_pred
output=pd.DataFrame({'PassengerId':df1['PassengerId'], 'Survived':y_pred})
output.head()
output.to_csv('/content/result.csv')

from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(n_estimators=500)
clf=clf.fit(x_new,y)
y_pred=clf.predict(test)
y_pred
output=pd.DataFrame({'PassengerId':df1['PassengerId'], 'Survived':y_pred})
output.head()
output.to_csv('/content/result2.csv')