import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
# This file show how the tensor flow 
# model trains it self with the input data set 
# predicts the output

# Generate random input data and corresponding random values
np.random.seed(0)  # For reproducibility

X = np.random.rand(100, 1)  # Random input data
Y = np.random.rand(100, 1)  # Corresponding random values
# Z = np.random.rand(100,1)
# x = []
# y = []

# for i in range(100):
#     x.append(X[i][0])
#     y.append(Y[i][0])

# plt.plot(x,y)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Graph of random numbers")
# plt.show()



# Create a simple feedforward neural network
model = keras.Sequential([
    keras.layers.Input(shape=(1,)),  # Input layer with 1 input node
    keras.layers.Dense(10, activation='relu'),  # Hidden layer with 10 nodes and ReLU activation
    keras.layers.Dense(1)  # Output layer with 1 node (regression problem)
])

# Compile the model for regression
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, Y, epochs=1000, verbose=0)

# Evaluate the model (not necessary for this random data)
loss = model.evaluate(X, Y)
print(f"Loss: {loss:.4f}")

# Make predictions on new random input data
new_X = np.random.rand(10, 1)
predictions = model.predict(new_X)



# Display the predictions
print("Predictions:")
for i in range(len(new_X)):
    print(f"Input: {new_X[i][0]:.4f}, \nPredicted Output: {predictions[i][0]:.4f}")
