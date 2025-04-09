# Bachelor of Science in Computer Science - Third Year - Block B
# Programming Language 101 - Tu.Th 08:30 AM-10:00 AM ABa 101
# Instructor: Mr. Ian Godwin Agapito
# Activity 3 - Midterm Activity
# (Individual) Generate a 5x5 random NumPy array and perform:
# Mean, median, and standard deviation calculations.
# Element-wise operations with another array.
# Reshaping the array into a different dimension.

import numpy as np

# Generate a 5x5 random array with integers between 0 and 100
array1 = np.random.randint(0, 100, size=(5, 5))

# Print the original array
print("Original 5x5 Random Array:")
print(array1)

# Task 1: Calculate mean, median, and standard deviation
print("\nTask 1: Statistical Calculations")
print("Mean:", np.mean(array1))
print("Median:", np.median(array1))
print("Standard Deviation:", np.std(array1))

# Task 2: Element-wise operations with another array
# Create a second 5x5 random array
array2 = np.random.randint(0, 100, size=(5, 5))
print("\nTask 2: Element-wise Operations")
print("Second 5x5 Random Array:")
print(array2)
print("Addition (array1 + array2):")
print(array1 + array2)
print("Multiplication (array1 * array2):")
print(array1 * array2)

# Task 3: Reshape the array into a different dimension
# Reshape the 5x5 array (25 elements) into a 1x25 array
reshaped_array = array1.reshape(1, 25)
print("\nTask 3: Reshaping")
print("Reshaped to 1x25:")
print(reshaped_array)
# Reshape into a 25x1 array
reshaped_array2 = array1.reshape(25, 1)
print("Reshaped to 25x1:")
print(reshaped_array2)