# Using the classic MNIST dataset. I'm gonna build a CNN from scratch (throwback to chem277b).
# Code based on Chapter 3 of Deep Learning for the Life Sciences: Applying Deep Learning to Genomics, Microscopy, Drug Discovery, and More by Bharath Ramsundar

# doing this to ensure deepchem uses Keras 2 instead of Keras 3
import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import deepchem as dc
import tensorflow as tf
import tensorflow.keras.layers as layers

# load dataset, one hot encode labels
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
y_train = tf.one_hot(y_train, 10).numpy()
y_test = tf.one_hot(y_test, 10).numpy()

# construct NumpyDataset object to split training and test sets
training_dataset = dc.data.NumpyDataset(x_train, y_train)
testing_dataset = dc.data.NumpyDataset(x_test, y_test)

features = tf.keras.Input(shape = (28, 28, 1))
conv2d_1 = layers.Conv2D(filters = 32,
                         kernel_size = 5,
                         activation = tf.nn.relu)(features)
conv2d_2 = layers.Conv2D(filters = 64,
                         kernel_size = 5,
                         activation = tf.nn.relu)(conv2d_1)
flatten = layers.Flatten()(conv2d_2) # flatten input 2D -> 1D
dense1 = layers.Dense(units = 1024,
                      activation = tf.nn.relu)(flatten)
dense2 = layers.Dense(units = 10,
                      activation = None)(dense1)
# apply softmax to dense2
output = layers.Activation(tf.math.softmax)(dense2) # computing softmax & cross entropy in same step is more "numerically stable"

# make tensorflow keras model, wrap in deepchem model
tf_keras_model = tf.keras.Model(inputs = features, outputs = [output, dense2])
dc_model = dc.models.KerasModel(
    tf_keras_model,
    loss = dc.models.losses.SoftmaxCrossEntropy(),
    output_types = ['prediction', 'loss'],
    model_dir = 'mnist')

# doing this to ensure that deepchem uses Keras 2 instead of Keras 3
TF_USE_LEGACY_KERAS = True

# train and evaluate model
dc_model.fit(training_dataset, nb_epoch = 100)

# define evaluation metric. Evaluate and print scores
metric = dc.metrics.Metric(dc.metrics.accuracy_score)
training_score = dc_model.evaluate(training_dataset, [metric])
testing_score = dc_model.evaluate(testing_dataset, [metric])

print(f"Training score is {training_score}")
print(f"Testing score is {testing_score}")