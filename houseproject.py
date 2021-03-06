# -*- coding: utf-8 -*-
"""houseproject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iB8TwM-I_BBT0eJIsEh6GEmBOJ65qVsx
"""

import pandas as pd
data=pd.read_csv("/content/Housing_Modified.csv")
data.shape

data.corr()

import sklearn.preprocessing as pp

lb=pp.LabelBinarizer()
data.driveway = lb.fit_transform(data.driveway)
data.recroom = lb.fit_transform(data.recroom)
data.fullbase = lb.fit_transform(data.fullbase)
data.airco = lb.fit_transform(data.airco)
data.gashw = lb.fit_transform(data.gashw)
data.prefarea = lb.fit_transform(data.prefarea)

data.corr()

encoder=pp.LabelEncoder()
data.stories = encoder.fit_transform(data.stories)
data.stories

data.corr()

import matplotlib.pyplot as plt
data.plot()

Xnorm = (data.price - min_price)/(max_price-min_price)

ind_columns = data.columns
ind_columns.delete(0)

X = data[ind_columns]
Xnorm = (X- X.min())/(X.max()-X.min())
Xnorm.plot()

import seaborn as sns
corr = data.corr()
mask = 
size = max(10, len(corr.columns)/2.)
f,ax = plt.subplots(figsize=(size,size))
sns.heatmap(corr, annot=True, mask=mask, square=True, linewidths=.5, cbar_kws={"shrink": 0.5}, ax=ax)

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
mm = MinMaxScaler()
mm.fit_transform(X)

ss= StandardScaler()
ss.fit_transform(X)

plt.scatter(data["lotsize"], data["price"], color="red")

Y= data.price
independent = data.columns
independent = independent.delete(0)
X = data[independent]

import sklearn.linear_model as lm
model = lm.LinearRegression()

model = model.fit(X , Y )

print("The slope(m) of equation is", model.coef_)
print("The intercept/residue (c) is", model.intercept_)

Ypred = model.predict(X)

from sklearn.metrics import  r2_score, mean_absolute_error , mean_squared_error

r2_score(Y, Ypred)

from statsmodels.stats.outliers_influence import variance_inflation_factor as vif

for i in range(len(independent)):
  vif_list = [vif(data[independent].values, index) for index in range(len(independent))]
  mvif = max(vif_list)
  print("Max VIF value:",mvif)
  drop_index = vif_list.index(mvif)
  if mvif > 10:
    print("deleting", independent[drop_index])
    independent = independent.delete(drop_index)
print("Final Independent Variables", independent)

import statsmodels.api as sm
Y = data["price"]
X = data[independent]
model = sm.OLS(Y,X)
model = model.fit()
model.summary()

user_input = {}
for var in independent:
  temp = input("Enter " +var+": ")
  user_input[var] = temp
user_df = pd.DataFrame(data=user_input, index=[0], columns=independent)
import sklearn.linear_model as lm
lr=lm.LinearRegression()
lr.fit(X,Y)
price = lr.predict(user_df)

print("Price of House is USD", int(price[0]))