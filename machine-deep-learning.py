from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.datasets import load_iris
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pa
from keras.optimizers import Adam

iris_data = load_iris()

features = iris_data.data
labels = np.array(iris_data.target).reshape(-1, 1)

encoder = OneHotEncoder(sparse=False)
targets = encoder.fit_transform(labels) #

features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.2)

model = Sequential()
model.add(Dense(10, input_dim=3, activation='relu'))
model.add(Dense(10, input_dim=10, activation='relu'))
model.add(Dense(10, input_dim=10, activation='relu'))
model.add(Dense(2, activation='sigmoid'))

optimizer = Adam(learning_rate=0.001)
model.compile(loss='categorical_croosentropy', optimizer=optimizer, metrics=['accuracy'])

model.fit(features_train, targets_train, epochs=1000, batch_size=20, verbose=2)

results = model.evaluate(features_test, targets_test)

print(results)