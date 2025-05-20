# In the previous exercise, you wrote a function that transposed a 3x3 matrix represented by a list of lists.

# Matrix transposes are not limited to 3x3 matrices, or even square matrices. Any matrix can be transposed simply by switching columns with rows.

# Modify your transpose function from the previous exercise so that it works with any MxN matrix with at least one row and one column.

def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    return [[matrix[j][i] for j in range(rows)] for i in range(columns)]

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)
