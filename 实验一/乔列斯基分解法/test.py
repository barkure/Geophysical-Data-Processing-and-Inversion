# Description: 乔列斯基分解
from cholesky_decomposition import cholesky_decomposition

A = [[6, 3, -2], [3, 5, 1], [-2, 1, 7]]
b = [1, 1, 1]
print("-" * 50)
x = cholesky_decomposition(A, b)
print("-" * 50, "\n方程组的解为：\n", "-" * 50)
print(x)
print("-" * 50)