# Description: 辛普森法数值积分

import sympy as sp

def intsimpson(f, a, b, type, eps=None):
    if type == 3 and eps is None:
        print('缺少参数')
        return None, None

    x = sp.symbols('x')
    q = 0
    step = 0

    if type == 'simpson':
        q = ((b - a) / 6) * (f.subs(x, a) + 4 * f.subs(x, (a + b) / 2) + f.subs(x, b))
        step = 1
    elif type == '3/8':
        q = ((b - a) / 8) * (f.subs(x, a) + 3 * f.subs(x, (2 * a + b) / 3) +
                               3 * f.subs(x, (a + 2 * b) / 3) + f.subs(x, b))
        step = 1
    elif type == 'composite_simpson':
        n = 2
        h = (b - a) / 2
        q1 = 0
        q2 = (f.subs(x, a) + f.subs(x, b)) / h
        while float(abs(q2 - q1)) > eps:
            n += 1
            h = (b - a) / n
            q1 = q2
            q2 = 0
            for i in range(n):
                xi = a + i * h
                q2 += (h / 6) * (f.subs(x, xi) +
                                 4 * f.subs(x, (xi + (a + i * h)) / 2) +
                                 f.subs(x, a + i * h))
        q = q2
        step = n

    return q, step
