from keras.models import Sequential
from keras.layers import Dense
import numpy as np

features = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], 'float32')
targets = np.array([[0], [1], [1], [0]], 'float32')

model = Sequential()
model.add(Dense(2, input_dim=16, activation='relu'))
model.add(Dense(16, input_dim=16, activation='relu'))
model.add(Dense(16, input_dim=16, activation='relu'))
model.add(Dense(16, input_dim=16, activation='relu'))
model.add(Dense(16, input_dim=16, activation='relu'))
model.add(Dense(16, input_dim=16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))