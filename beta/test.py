# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 23:59:13 2018

@author: hp
"""
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score

ds = pd.read_csv('text_emotion.csv')
#ds.head()

stopset = set(stopwords.words('english'))
vectorizer = TfidfVectorizer(use_idf = True, lowercase=True, strip_accents='ascii', stop_words=stopset)

y = ds.sentiment

for i in range(len(y)):
    if y[i] == 'sadness':
        y[i] = 1
    else:
        y[i] = 0

y = y.astype(str).astype(int)
#y = y.astype(str)
        
X = vectorizer.fit_transform(ds.content)

#print(x,y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3 random_state=42)

clf = naive_bayes.MultinomialNB()
clf.fit(X_train,y_train)

roc_auc_score(y_test, clf.predict_proba(X_test)[:,1])



r = np.array(["I am not sad today."])
rv = vectorizer.transform(r)

print( clf.predict(rv))