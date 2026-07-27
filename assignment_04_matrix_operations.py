# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================

# -------------------------------
# Utility: Display matrix neatly
# -------------------------------
def display_matrix(matrix):
    for row in matrix:
        for val in row:
            print(f"{val:5}", end="")  # aligned spacing
        print()
    print()

# -------------------------------
# Part A: Transpose a Matrix
# -------------------------------
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transpose.append(new_row)
    return transpose

# -------------------------------
# Part B: Add Two Matrices
# -------------------------------
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(matrix1[r][c] + matrix2[r][c])
        result.append(new_row)
    return result

# -------------------------------
# Part C: Multiply Two Matrices
# -------------------------------
def multiply_matrices(matrixA, matrixB):
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    rowsB = len(matrixB)
    colsB = len(matrixB[0])

    if colsA != rowsB:
        print("Error: Cannot multiply, incompatible dimensions.")
        return None

    result = []
    for i in range(rowsA):
        new_row = []
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += matrixA[i][k] * matrixB[k][j]
            new_row.append(total)
        result.append(new_row)
    return result

# -------------------------------
# Helper: Read matrix from user
# -------------------------------
def read_matrix(rows, cols):
    matrix = []
    for r in range(rows):
        row_values = input(f"Enter row {r+1}: ").split()
        row = [int(val) for val in row_values]
        if len(row) != cols:
            print("Error: Row length mismatch.")
            return None
        matrix.append(row)
    return matrix

# -------------------------------
# Main Program
# -------------------------------
def main():
    # Part A: Transpose
    print("=== Part A: Transpose ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix = read_matrix(m, n)
    print("\nOriginal Matrix:")
    display_matrix(matrix)
    transposed = transpose_matrix(matrix)
    print("Transposed Matrix:")
    display_matrix(transposed)

    # Part B: Addition
    print("=== Part B: Add Two Matrices ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    print("Matrix 1:")
    matrix1 = read_matrix(m, n)
    print("Matrix 2:")
    matrix2 = read_matrix(m, n)
    print("\nSum of Matrices:")
    display_matrix(add_matrices(matrix1, matrix2))

    # Part C: Multiplication
    print("=== Part C: Multiply Two Matrices ===")
    m = int(input("Enter rows for Matrix A: "))
    n = int(input("Enter columns for Matrix A: "))
    matrixA = read_matrix(m, n)

    p = int(input("Enter columns for Matrix B: "))
    print("Matrix B:")
    matrixB = read_matrix(n, p)

    print("\nMatrix A:")
    display_matrix(matrixA)
    print("Matrix B:")
    display_matrix(matrixB)

    product = multiply_matrices(matrixA, matrixB)
    if product:
        print("Product Matrix:")
        display_matrix(product)

# Run program
if __name__ == "__main__":
    main()

