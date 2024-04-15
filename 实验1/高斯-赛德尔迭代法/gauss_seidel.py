# Description: 高斯-赛德尔迭代法
import numpy as np

def gauss_seidel(A, b, x0=None, eps=1e-10, M=1000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    if x0 is None:
        x = np.zeros_like(b)
    else:
        x = np.array(x0, dtype=float)
    n = 0
    for _ in range(M):
        x_new = np.copy(x)
        for i in range(A.shape[0]):
            x_new[i] = (b[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, i + 1:], x_new[i + 1:])) / A[i, i]
        if np.allclose(x, x_new, rtol=eps):
            break
        x = x_new
        n += 1
    return x, n