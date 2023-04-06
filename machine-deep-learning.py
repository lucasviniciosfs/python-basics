from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

import numpy as np
import pandas as pa

data = pa.read_csv('credit_data.csv')

features = data[['income','age','loan']]
labels = np.array(data.default).reshape(-1, 1)

features_train, features_test, labes_train, labels_test = train_test_split(features, labels, train_size=0.25)

encoder = OneHotEncoder()
targets = encoder.fit_transform(labels).toarray()

print(targets)