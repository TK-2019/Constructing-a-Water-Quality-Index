# -*- coding: utf-8 -*-
"""training.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10PCT2d87jZ8kEZeG41-YKvppzzwIbFaB

# Training a Neural Network for Water Quality Classification

This notebook demonstrates the process of training a neural network to classify water quality into 'healthy' or 'unhealthy' categories based on specific parameters.

## Steps Covered:
1. Loading and exploring the dataset
2. Preprocessing the data (handling missing values, encoding, and scaling)
3. Splitting the data into training, validation, and testing sets
4. Building and training a neural network
5. Evaluating the model performance
"""

import tensorflow as tf
import pandas as pd
# Split the dataset into training, validation, and testing sets
from sklearn.model_selection import train_test_split
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

# Load the dataset into a Pandas DataFrame
data = pd.read_csv('/content/training_data.csv')
print(data.head())

X = data.drop('Health_Status', axis=1)
y = data['Health_Status']

# Split the dataset into training, validation, and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Split the dataset into training, validation, and testing sets
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42, stratify=y_train)

print(X_train.shape)
print(X_val.shape)
print(X_test.shape)
print(y_train.shape)
print(y_val.shape)
print(y_test.shape)

# Define the architecture of the neural network
model = Sequential([
    Dense(64, input_shape=(9,)),
    Activation('relu'),
    Dense(32),
    Activation('relu'),
    Dense(16),
    Activation('relu'),
    Dense(8),
    Activation('relu'),
    Dense(1),
    Activation('sigmoid')
])

model.save('model.h5')

# Compile the model with a loss function, optimizer, and metrics
model.compile(optimizer='adam',
              loss='binary_crossentropy' ,
              metrics=['accuracy'])

# Train the model with the training data and validate on the validation set
history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_data=(X_val, y_val),
    callbacks=[tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)]
)

# Evaluate the model on the test set to check generalization performance
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=1)
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")

weights = model.get_weights()

input_weights = model.layers[0].get_weights()[0]
print(input_weights.shape)

feature_importance = np.mean(np.abs(input_weights), axis=1)
print(feature_importance.shape)

normalized_importance = feature_importance / np.sum(feature_importance)
print(normalized_importance)

print(np.sum(normalized_importance))
