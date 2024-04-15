# Description：Newton interpolation
import numpy as np

# divided difference
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y

    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
            
    return coef

# Newton interpolation
def Newton(x, y, x0):
    coef = divided_diff(x, y)
    n = len(x) - 1 
    p = coef[0, n]
    for k in range(1, n + 1):
        p = coef[0, n - k] + (x0 - x[n - k]) * p
    return p
