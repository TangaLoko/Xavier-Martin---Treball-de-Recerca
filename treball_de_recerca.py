# -*- coding: utf-8 -*-
"""Treball de Recerca.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MmNGPHxN6Y618DjP5wFA45njh7zc1c7c
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):           #funcion a predecir
  return 3.1415 * (x**2) + 42


import tensorflow as tf

modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=6, input_shape=[1], activation='softplus'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(units=10, activation='sigmoid'),
    tf.keras.layers.Dense(units=14, activation='relu'),
    tf.keras.layers.Dense(units=14, activation='relu'),
    tf.keras.layers.Dense(units=10, activation='sigmoid'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(units=6, activation='softplus'),
    tf.keras.layers.Dense(units=1)
])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss='mean_squared_error'
)

x = np.linspace(-10, 10, 500)
y = f(x)

historial = modelo.fit(x, y, epochs=1000, verbose=True)

x_pred = np.linspace(-20, 20, 500)
y_pred = modelo.predict(x_pred)

x_total = np.linspace (-20, 20, 500)
y_total = f(x_total)

plt.figure()
plt.xlabel("Epoch")
plt.ylabel("Cost Function")
plt.title("History loss")
plt.plot(historial.history["loss"])
plt.show()

x_pred = np.linspace(-9.4, 9.4, 500)
y_pred = modelo.predict(x_pred)

x_total = np.linspace (-10, 10, 500)
y_total = f(x_total)

plt.figure()
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Comparison")
plt.plot(x, y, 'y', label="Training function")
plt.plot(x_pred, y_pred, 'b', label="Predicted function")
plt.plot(x_total, y_total, 'g', label= "Expected function")
plt.legend()
plt.show()