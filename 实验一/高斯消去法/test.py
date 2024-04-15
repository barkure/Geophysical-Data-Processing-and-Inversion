# Description: 高斯消去法测试
from column_pivoting import column_pivoting_gauss_elimination
from complete_pivoting import complete_pivoting_gauss_elimination
import numpy as np

# 测试列主元高斯消去法
A = np.array([[3, 6, 0], [7, -2, 5], [2, 1, 8]], dtype=float)
b = np.array([1, 1, 1], dtype=float)
x = column_pivoting_gauss_elimination(A, b)
print("-" * 50)
print("线性方程组的解（列主元高斯消去法）：")
print("-" * 50)
print(x)

# 测试完全主元高斯消去法
A = np.array([[10, 6, 4], [5, 0, 1], [2, -1, 8]], dtype=float)
b = np.array([1, 1, 1], dtype=float)
x = complete_pivoting_gauss_elimination(A, b)
print("-" * 50)
print("线性方程组的解（完全主元高斯消去法）：")
print("-" * 50)
print(x)
print("-" * 50)
