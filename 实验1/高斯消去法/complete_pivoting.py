# Description：完全主元高斯消去法
import numpy as np
from solve_upper_triangular import solve_upper_triangular

def complete_pivoting_gauss_elimination(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A)
    M = np.column_stack((A, b))
    for k in range(n):
        maxindex = abs(M[k:,k]).argmax() + k
        if M[maxindex, k] == 0:
            raise ValueError("Matrix is singular.")
        M[[k, maxindex]] = M[[maxindex, k]]
        for row in range(k+1, n):
            multiplier = M[row][k]/M[k][k]
            M[row, k:] -= multiplier * M[k, k:]
    upper_triangular = M[:,:-1]
    new_b = M[:,-1]
    x = solve_upper_triangular(upper_triangular, new_b)
    return x