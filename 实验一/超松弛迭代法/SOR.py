# Description: SOR迭代法
import numpy as np

def SOR(A, b, x0=None, w=1.0, eps=1e-10, M=1000):
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
            old_sum = np.dot(A[i, :i], x_new[:i]) + np.dot(A[i, i + 1:], x_new[i + 1:])
            x_new[i] = (1 - w) * x_new[i] + (w / A[i, i]) * (b[i] - old_sum)
        if np.allclose(x, x_new, rtol=eps):
            break
        x = x_new
        n += 1
    return x, n