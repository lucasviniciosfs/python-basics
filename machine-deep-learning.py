from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pa
from keras.optimizers import Adam

data = pa.read_csv('credit_data.csv')

features = data[['income','age','loan']]
labels = np.array(data.default).reshape(-1, 1)

encoder = OneHotEncoder()
targets = encoder.fit_transform(labels).toarray()

features_train, features_test, targets_train, targets_test = train_test_split(features, targets, train_size=0.2)

model = Sequential()
model.add(Dense(10, input_dim = 3, activation="sigmoid"))
model.add(Dense(2, activation='softmax'))

optimizer = Adam(0.001)
model.compile(
    loss='categorical_crossentropy',
    optimizer=optimizer,
    metrics=['accuracy']
)

model.fit(features_train, targets_train, epochs=10000, verbose=2)
result = model.evaluate(features_test, targets_test, use_multiprocessing=True)

print(result)