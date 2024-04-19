import numpy as np
from sympy import symbols, integrate

def IntGauss(f, a, b, n, AK=None, XK=None):
    x = symbols('x')
    f = f.subs(x, ((b-a)/2)*x + (b+a)/2)
    if n > 5:
        if AK is None or XK is None:
            raise ValueError("AK and XK must be provided when n > 5")
        q = ((b-a)/2) * sum(AK * f.subs(x, XK))
    else:
        if n == 1:
            q = 2 * f.subs(x, (b+a)/2)
        elif n == 2:
            q = ((b-a)/2) * (f.subs(x, -1/np.sqrt(3)) + f.subs(x, 1/np.sqrt(3)))
        else:
            raise ValueError("n must be 1, 2 or greater than 5")
    ta = (b-a)/2
    tb = (b+a)/2
