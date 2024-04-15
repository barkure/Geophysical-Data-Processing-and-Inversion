# Description: SOR迭代法测试
from SOR import SOR

A = [[0.68, 0.01, 0.12],
     [0.03, -0.54, -0.05],
     [0.2, 0.08, 0.74]]
b = [1, 1, 1]
x0 = [0, 0, 0]
w = 1.07  # 松弛因子w为1.07

x, n = SOR(A, b, x0, w)
print("Solution: ", x)
print("Number of iterations: ", n)