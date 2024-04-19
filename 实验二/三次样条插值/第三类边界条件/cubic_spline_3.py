# Description: 第三类边界条件三次样条插值
import numpy as np

def solve_up_triangle(A, b):
    n = len(A)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        s = np.dot(A[i, i+1:], x[i+1:])
        x[i] = (b[i] - s) / A[i, i]
    return x

def cubic_spline_3(x, y, x0):
    n = len(x)
    if n != len(y):
        print('x和y的维数不相等')
        return None, None

    index = np.where((x <= x0) & (np.roll(x, -1) >= x0))[0][0]

    A = 2 * np.eye(n-1)
    h0 = x[1] - x[0]
    h1 = x[2] - x[1]
    he = x[-1] - x[-2]
    A[0, 1] = h0 / (h0 + h1)
    A[0, -1] = 1 - A[0, 1]
    A[-1, 0] = he / (h0 + he)
    A[-1, -2] = 1 - A[-1, 0]

    c = np.zeros(n-1)
    c[0] = 3 * A[0, -1] * (y[1] - y[0]) / h0 + 3 * A[0, 1] * (y[2] - y[1]) / h1
    for i in range(1, n-2):
        u = (x[i] - x[i-1]) / (x[i+1] - x[i-1])
        lamda = (x[i+1] - x[i]) / (x[i+1] - x[i-1])
        c[i] = 3 * lamda * (y[i] - y[i-1]) / (x[i] - x[i-1]) + 3 * u * (y[i+1] - y[i]) / (x[i+1] - x[i])
        A[i, i+1] = u
        A[i, i-1] = lamda
    c[-1] = 3 * (he * (y[1] - y[0]) / h0 + h0 * (y[-1] - y[-2]) / he) / (h0 + he)

    m = np.zeros(n)
    m[1:] = solve_up_triangle(A, c)
    m[0] = m[-1]

    h = x[index+1] - x[index]
    f = lambda t: y[index] * (2 * (t - x[index]) + h) * (t - x[index+1])**2 / h**3 + \
                  y[index+1] * (2 * (x[index+1] - t) + h) * (t - x[index])**2 / h**3 + \
                  m[index] * (t - x[index]) * (x[index+1] - t)**2 / h**2 - \
                  m[index+1] * (x[index+1] - t) * (t - x[index])**2 / h**2
    f0 = f(x0)
    return f, f0