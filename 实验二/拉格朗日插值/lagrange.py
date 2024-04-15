# Description: Lagrange interpolation

def Language(x, y, x0):
    n = len(x)
    f = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x0 - x[j]) / (x[i] - x[j])
        f += y[i] * L
    return f

