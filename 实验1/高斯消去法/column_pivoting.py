# Description：列主元高斯消去法
import numpy as np
from solve_upper_triangular import solve_upper_triangular

def column_pivoting_gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        # 寻找最大的主元
        max_row = np.argmax(np.abs(A[i:, i])) + i
        # 交换行以确保最大的主元在 (i, i) 位置
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]
        # 消元
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    # 回代求解
    x = solve_upper_triangular(A, b)
    return x
