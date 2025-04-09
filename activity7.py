# Import NumPy and the math module
import numpy as np
import math

# Generate an array of 10 random numbers between 0 and 100
array = np.random.uniform(1, 100, size=10)  # Using uniform for positive numbers

# Print the original array
print("Original Array:")
print(array)

# Apply mathematical operations
# Square root
sqrt_array = np.sqrt(array)
print("\nSquare Root of Each Value:")
print(sqrt_array)

# Natural logarithm (log base e)
log_array = np.log(array)
print("\nNatural Logarithm of Each Value:")
print(log_array)

# Exponential (e^x)
exp_array = np.exp(array)
print("\nExponential (e^x) of Each Value:")
print(exp_array)