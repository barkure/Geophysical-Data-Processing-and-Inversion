# Description: 雅可比迭代法
import numpy as np

def jacobi(A, b, x0=None, eps=1e-6, M=1000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    if x0 is None:
        x = np.zeros_like(b)
    else:
        x = np.array(x0, dtype=float)
    # n 是迭代次数
    n = 0
    for _ in range(M):
        x_new = (b - np.dot(A, x) + np.diag(A)*x) / np.diag(A)
        if np.allclose(x, x_new, rtol=eps):
            break
        x = x_new
        n += 1
    return x, n