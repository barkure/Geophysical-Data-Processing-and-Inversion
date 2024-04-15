# Description: 复合梯形公式
def CombineTraprl(f, a, b, eps):
    step = 1
    h = b - a
    I_old = 0.5 * h * (f(a) + f(b))
    
    while True:
        h /= 2
        I_new = 0.5 * I_old + h * sum(f(a + i*h) for i in range(1, 2*step, 2))
        if abs(I_new - I_old) < eps:
            return I_new, 2*step
        I_old = I_new
        step *= 2