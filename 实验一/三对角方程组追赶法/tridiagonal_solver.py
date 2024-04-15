# Description: 三对角方程组追赶法
import numpy as np

def tridiagonal_solver(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A)
    a = np.zeros(n-1, dtype=float)
    c = np.zeros(n-1, dtype=float)
    b_main = np.zeros(n, dtype=float)
    for i in range(n):
        if i < n - 1:
            a[i] = A[i+1, i]
            c[i] = A[i, i+1]
        b_main[i] = A[i, i]
    w = np.zeros(n-1,float)
    g = np.zeros(n, float)
    p = np.zeros(n,float)

    w[0] = c[0]/b_main[0]
    g[0] = b[0]/b_main[0]

    for i in range(1,n-1):
        w[i] = c[i]/(b_main[i] - a[i-1]*w[i-1])
    for i in range(1,n):
        g[i] = (b[i] - a[i-1]*g[i-1])/(b_main[i] - a[i-1]*w[i-1])
    p[n-1] = g[n-1]
    for i in range(n-1,0,-1):
        p[i-1] = g[i-1] - w[i-1]*p[i]
    return p
