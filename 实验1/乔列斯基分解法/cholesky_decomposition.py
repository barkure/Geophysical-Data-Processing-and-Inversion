# Description：乔列斯基分解
import numpy as np
from solve_upper_triangular import solve_upper_triangular
from solve_lower_triangular import solve_lower_triangular

def cholesky_decomposition(A, b):
    A = np.array(A, dtype=float)
    n = len(A)
    L = np.zeros_like(A)
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            if (i == k): # 对角线元素
                L[i][k] = np.sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    print("乔列斯基分解得到的 L 矩阵: \n", "-" * 50)
    print(L)
    y = solve_lower_triangular(L, b)
    L_Transpose = L.T # 转置
    x = solve_upper_triangular(L_Transpose, y)
    return x
    