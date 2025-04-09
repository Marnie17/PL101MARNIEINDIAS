# Bachelor of Science in Computer Science - Third Year - Block B
# Programming Language 101 - Tu.Th 08:30 AM-10:00 AM ABa 101
# Instructor: Mr. Ian Godwin Agapito
# Activity 6 - Midterm Activity
# (Challenge): Create a function that takes two NumPy arrays and performs matrix multiplication, handling exceptions for mismatched dimensions.

# Matrix Multiplication Application
# Performs matrix multiplication between two NumPy arrays using a GUI interface
# Handles exceptions for mismatched dimensions


    
import numpy as np

def parse_matrix(text_input):
    """Parse matrix from text input"""
    try:
        # Split by lines and then by spaces
        lines = text_input.strip().split('\n')
        matrix = []
        
        for line in lines:
            if line.strip():  # Skip empty lines
                row = [float(x) for x in line.strip().split()]
                matrix.append(row)
        
        # Check if all rows have the same number of elements
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise ValueError("All rows must have the same number of elements")
            
        return np.array(matrix)
    except ValueError as e:
        raise ValueError(f"Invalid matrix format: {str(e)}")

def matrix_multiply(matrix_a, matrix_b):
    """
    Performs matrix multiplication between two NumPy arrays.
    Handles exceptions for mismatched dimensions.
    """
    try:
        # Check dimensions compatibility
        if matrix_a.shape[1] != matrix_b.shape[0]:
            raise ValueError(f"Matrix dimensions are incompatible for multiplication: "
                           f"{matrix_a.shape} and {matrix_b.shape}. "
                           f"The number of columns in Matrix A ({matrix_a.shape[1]}) must equal "
                           f"the number of rows in Matrix B ({matrix_b.shape[0]})")
        
        # Perform matrix multiplication
        result = np.matmul(matrix_a, matrix_b)
        return result
    
    except Exception as e:
        raise Exception(f"Multiplication error: {str(e)}")

def get_matrix_input(matrix_name):
    """Helper function to get matrix input from user"""
    print(f"\nEnter {matrix_name}:")
    print("Enter each row with space-separated numbers")
    print("Press Enter after each row")
    print("Enter an empty line (just press Enter) when finished")
    
    lines = []
    while True:
        line = input("Row: ")
        if line.strip() == "":  # Empty line signals end of input
            if not lines:  # If no lines entered yet, continue asking
                print("Please enter at least one row")
                continue
            break
        lines.append(line)
    
    return "\n".join(lines)

def main():
    print("Matrix Multiplication Program")
    print("===================================")
    
    while True:
        try:
            # Get matrices
            matrix_a_input = get_matrix_input("Matrix A")
            matrix_b_input = get_matrix_input("Matrix B")
            
            # Parse matrices
            matrix_a = parse_matrix(matrix_a_input)
            matrix_b = parse_matrix(matrix_b_input)
            
            # Display input matrices
            print("\nMatrix A:")
            print(matrix_a)
            print("Shape:", matrix_a.shape)
            
            print("\nMatrix B:")
            print(matrix_b)
            print("Shape:", matrix_b.shape)
            
            # Perform multiplication
            result = matrix_multiply(matrix_a, matrix_b)
            
            # Display results
            print("\nResult (A × B):")
            print(result)
            print("Shape:", result.shape)
            
            # Display properties
            print("\nProperties:")
            print(f"Determinant (if square): {np.linalg.det(result) if result.shape[0] == result.shape[1] else 'N/A'}")
            print(f"Trace (if square): {np.trace(result) if result.shape[0] == result.shape[1] else 'N/A'}")
            print(f"Rank: {np.linalg.matrix_rank(result)}")
            
            break  # Exit loop if successful
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            retry = input("\nWould you like to try again? (y/n): ").lower()
            if retry != 'y':
                break

if __name__ == "__main__":
    main()