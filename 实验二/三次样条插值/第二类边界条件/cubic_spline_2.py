# Description: 第二类边界条件三次样条插值
import numpy as np
from sympy import symbols

def cubic_spline_2(x, y, y2_1, y2_N, x0):
    t = symbols('t')
    f = 0.0
    f0 = 0.0
    if len(x) != len(y):
        print('x和y的维数不相等')
        return
    n = len(x)
    index = next(i for i in range(n) if x[i] <= x0 and x[i+1] >= x0)
    A = 2 * np.eye(n)
    A[0, 1] = 1
    A[n-1, n-2] = 1
    u = np.zeros(n-2)
    lamda = np.zeros(n-1)
    c = np.zeros(n)
    for i in range(1, n-1):
        u[i-1] = (x[i] - x[i-1]) / (x[i+1] - x[i-1])
        lamda[i] = (x[i+1] - x[i]) / (x[i+1] - x[i-1])
        c[i] = 3 * lamda[i] * (y[i] - y[i-1]) / (x[i] - x[i-1]) + 3 * u[i-1] * (y[i+1] - y[i]) / (x[i+1] - x[i])
        A[i, i+1] = u[i-1]
        A[i, i-1] = lamda[i]
    c[0] = 3 * (y[1] - y[0]) / (x[1] - x[0]) - (x[1] - x[0]) * y2_1 / 2
    c[n-1] = 3 * (y[n-1] - y[n-2]) / (x[n-1] - x[n-2]) - (x[n-1] - x[n-2]) * y2_N / 2
    m = np.linalg.solve(A, c)
    h = x[index+1] - x[index]
    f = y[index] * (2 * (t - x[index]) + h) * (t - x[index+1])**2 / h**3 + y[index+1] * (2 * (x[index+1] - t) + h) * (t - x[index])**2 / h**3 + m[index] * (t - x[index]) * (x[index+1] - t)**2 / h**2 - m[index+1] * (x[index+1] - t) * (t - x[index])**2 / h**2
    f0 = f.subs(t, x0)
    return f, f0