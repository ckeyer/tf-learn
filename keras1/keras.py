#!/usr/bin/env python3

import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

model = Sequential()
