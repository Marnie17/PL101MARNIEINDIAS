# MARNIE D. INDIAS
# Bachelor of Science in Computer Science - Third Year - Block B
# Programming Language 101 - Tu.Th 08:30 AM-10:00 AM ABa 101
# Instructor: Mr. Ian Godwin Agapito
# Activity 5 - Midterm Activity
# (Individual): Write a function that:
# Takes a NumPy array as input.
# Normalizes its values to a range between 0 and 1.
# Returns the modified array.


import numpy as np

# Define the normalization function
def normalize_array(arr):
    # Find the minimum and maximum values in the array
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    # Avoid division by zero (if max_val equals min_val)
    if max_val == min_val:
        return arr  # If all values are the same, return the original array
    else:
        # Normalize using the formula: (x - min) / (max - min)
        normalized = (arr - min_val) / (max_val - min_val)
        return normalized

# Test the function
# Create a sample 5x5 random array
array = np.random.randint(0, 100, size=(5, 5))

# Print the original array
print("Original Array:")
print(array)

# Normalize the array and print the result
normalized_array = normalize_array(array)
print("\nNormalized Array (values between 0 and 1):")
print(normalized_array)