import numpy as np

A = np.array([
    [1**2, 1+2, 2*1-3],
    [1+2, 2**2, 2*2-3],
    [2*1-3, 2*2-3, 3**2]
])

determinant = np.linalg.det(A)

trace = np.trace(A)

is_singular = determinant == 0

is_symmetric = np.all(A == A.T)

is_lower_triangular = np.all(np.triu(A, 1) == 0)

print(determinant, trace, is_singular, is_symmetric, is_lower_triangular)
