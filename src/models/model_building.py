import numpy as np
import pandas as pd
import pickle
import yaml

params = yaml.safe_load(open("params.yaml",'r'))['model_building']

from sklearn.ensemble import GradientBoostingClassifier

# fetch the data from data/processed
train_data = pd.read_csv('./data/features/train_tfidf.csv')

X_train = train_data.iloc[:,0:-1].values
y_train = train_data.iloc[:,-1].values

# Define and train the XGBoost model

clf = GradientBoostingClassifier(n_estimators=params['n_estimators'],learning_rate=params['learning_rate'])
clf.fit(X_train, y_train)

# save
pickle.dump(clf, open('model.pkl','wb'))

