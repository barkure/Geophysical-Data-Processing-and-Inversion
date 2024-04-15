# Description: Gauss-Seidel迭代法测试
from gauss_seidel import gauss_seidel

A = [[0.98, -0.05, -0.02],
     [-0.04, -0.9, 0.07],
     [-0.02, 0.09, 0.94]]
b = [1, 1, 1]
x0 = [0, 0, 0] # 初始值

x, n = gauss_seidel(A, b)
print("Solution: ", x)
print("Number of iterations: ", n)