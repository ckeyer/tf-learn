import os
import sys
import time
import gzip

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sklearn
import pandas as pd
import tensorflow as tf

from tensorflow import keras

print(sys.version_info)
for module in mpl, np, pd, sklearn, tf, keras:
  print(module.__name__, module.__version__)

# os.exit(1)

dirname = os.path.join('/data/datasets', 'fashion-mnist')
files = [
  'train-labels-idx1-ubyte.gz', 'train-images-idx3-ubyte.gz',
  't10k-labels-idx1-ubyte.gz', 't10k-images-idx3-ubyte.gz'
]
paths = []
for fname in files:
  paths.append(os.path.join('/data/datasets', 'fashion-mnist', fname))
print(paths)

with gzip.open(paths[0], 'rb') as lbpath:
  y_train_all = np.frombuffer(lbpath.read(), np.uint8, offset=8)

with gzip.open(paths[1], 'rb') as imgpath:
  x_train_all = np.frombuffer(
      imgpath.read(), np.uint8, offset=16).reshape(len(y_train_all), 28, 28)

with gzip.open(paths[2], 'rb') as lbpath:
  y_test = np.frombuffer(lbpath.read(), np.uint8, offset=8)

with gzip.open(paths[3], 'rb') as imgpath:
  x_test = np.frombuffer(
      imgpath.read(), np.uint8, offset=16).reshape(len(y_test), 28, 28)

# return (x_train, y_train), (x_test, y_test)

# fashion_mnist = keras.datasets.fashion_mnist
# (x_train_all, y_train_all), (x_test, y_test) = fashion_mnist.load_data()
x_valid, x_train = x_train_all[:5000], x_train_all[5000:]
y_valid, y_train = y_train_all[:5000], y_train_all[5000:]

print(x_valid.shape, y_valid.shape)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)



from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
# x_train: [None, 28, 28] -> [None, 784]
x_train_scaled = scaler.fit_transform(
  x_train.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28)
x_valid_scaled = scaler.transform(
  x_valid.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28)
x_test_scaled = scaler.transform(
  x_test.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28)




model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28, 28]))
for _ in range(20):
  model.add(keras.layers.Dense(100, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy",
              optimizer = keras.optimizers.SGD(0.01),
              metrics = ["accuracy"])





# Tensorboard, earlystopping, ModelCheckpoint
logdir = './dnn-callbacks'
if not os.path.exists(logdir):
  os.mkdir(logdir)
output_model_file = os.path.join(logdir,
                                 "fashion_mnist_model.h5")

callbacks = [
  keras.callbacks.TensorBoard(logdir),
  keras.callbacks.ModelCheckpoint(output_model_file,
                                  save_best_only = True),
  keras.callbacks.EarlyStopping(patience=5, min_delta=1e-3),
]
history = model.fit(x_train_scaled, y_train, epochs=10,
                    validation_data=(x_valid_scaled, y_valid),
                    callbacks = callbacks)





def plot_learning_curves(history):
  pd.DataFrame(history.history).plot(figsize=(8, 5))
  plt.grid(True)
  plt.gca().set_ylim(0, 3)
  plt.show()

plot_learning_curves(history)

# 1. 参数众多，训练不充分
# 2. 梯度消失 -> 链式法则 -> 复合函数f(g(x))




model.evaluate(x_test_scaled, y_test, verbose=0)