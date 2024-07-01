#HW15

def is_magic_square(matrix):
    n = len(matrix)
    sum_diag1 = sum(matrix[i][i] for i in range(n))
    sum_diag2 = sum(matrix[i][n - 1 - i] for i in range(n))
    
    if sum_diag1 != sum_diag2:
        return False
    
    for i in range(n):
        if sum(matrix[i]) != sum_diag1 or sum(matrix[j][i] for j in range(n)) != sum_diag1:
            return False
    
    return True

# Example usage
matrix = [
    [15, 8, 1],
    [5, 9, 6],
    [4, 7, 15]
]  # You can change the matrix
if is_magic_square(matrix):
    print("The matrix is a magic square.")
else:
    print("The matrix is not a magic square.")
