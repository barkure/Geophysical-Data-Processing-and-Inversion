# Description: 第一类边界条件三次样条插值
import numpy as np
from sympy import symbols


# 使用追赶法求解 Ax = b
def followup(A, b):
    n = np.linalg.matrix_rank(A)
    for i in range(n):
        if A[i, i] == 0:
            print('对角元素为0')
            return
    d = np.ones((n, 1))
    a = np.ones((n - 1, 1))
    c = np.ones((n - 1, 1))
    for i in range(n - 1):
        a[i, 0] = A[i + 1, i]
        c[i, 0] = A[i, i + 1]
        d[i, 0] = A[i, i]
    d[n - 1, 0] = A[n - 1, n - 1]
    for i in range(1, n):
        d[i, 0] = d[i, 0] - (a[i - 1, 0] / d[i - 1, 0]) * c[i - 1, 0]
        b[i, 0] = b[i, 0] - (a[i - 1, 0] / d[i - 1, 0]) * b[i - 1, 0]
    x = np.zeros((n, 1))
    x[n - 1, 0] = b[n - 1, 0] / d[n - 1, 0]
    for i in range(n - 2, -1, -1):
        x[i, 0] = (b[i, 0] - c[i, 0] * x[i + 1, 0]) / d[i, 0]
    return x

def cubic_spline_1(x, y, y_1, y_N, x0):
    t = symbols('t')
    f = 0.0
    f0 = 0.0
    n = len(x)
    if n != len(y):
        print('x和y的维数不相等')
        return
    index = next(i for i in range(n - 1) if x[i] <= x0 and x[i + 1] >= x0)
    A = 2 * np.eye(n)
    u = np.zeros((n - 2, 1))
    lamda = np.zeros((n - 1, 1))
    c = np.zeros((n, 1))
    for i in range(1, n - 1):
        u[i - 1] = (x[i] - x[i - 1]) / (x[i + 1] - x[i - 1])
        lamda[i] = (x[i + 1] - x[i]) / (x[i + 1] - x[i - 1])
        c[i] = 3 * lamda[i] * (y[i] - y[i - 1]) / (x[i] - x[i - 1]) + 3 * u[i - 1] * (y[i + 1] - y[i]) / (x[i + 1] - x[i])
        A[i, i + 1] = u[i - 1]
        A[i, i - 1] = lamda[i]
    c[0] = 2 * y_1
    c[n - 1] = 2 * y_N
    m = followup(A, c)
    h = x[index + 1] - x[index]
    f = y[index] * (2 * (t - x[index]) + h) * (t - x[index + 1])**2 / h**3 + y[index + 1] * (2 * (x[index + 1] - t) + h) * (t - x[index])**2 / h**3 + m[index] * (t - x[index]) * (x[index + 1] - t)**2 / h**2 - m[index + 1] * (x[index + 1] - t) * (t - x[index])**2 / h**2
    f0 = np.array([expr.subs(t, x0) for expr in f])
    return f, f0