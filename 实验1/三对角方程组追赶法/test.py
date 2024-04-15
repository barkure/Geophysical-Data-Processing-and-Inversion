# Description: 三对角方程组追赶法测试
from tridiagonal_solver import tridiagonal_solver

A = [[1, -3, 0, 0, 0],
     [8, 2, 0, 0, 0],
     [0, 6, 3, 7, 0],
     [0, 0, 12, 4, 9],
     [0, 0, 0, -4, 5]]
b = [1, 1, 1, 1, 1]
result = tridiagonal_solver(A, b)
print("-" * 60, "\n方程组的解为：（三对角方程组追赶法）")
print("-" * 60)
print(result)
print("-" * 60)