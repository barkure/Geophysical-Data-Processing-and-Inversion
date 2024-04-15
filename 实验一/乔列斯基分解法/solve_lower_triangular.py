# Description: 求解下三角线性方程组
import numpy as np

def solve_lower_triangular(A, b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n):
        x[i] = (b[i] - np.dot(A[i, :i], x[:i])) / A[i, i]
    return x
