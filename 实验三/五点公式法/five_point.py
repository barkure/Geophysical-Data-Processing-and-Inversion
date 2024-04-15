# Description: 五点公式法

def FivePoint(func, x0, type, h):
    if type == 'forward1':
        df = (-25*func(x0) + 48*func(x0 + h) - 36*func(x0 + 2*h) + 16*func(x0 + 3*h) - 3*func(x0 + 4*h)) / (12*h)
    elif type == 'forward2':
        df = (-3*func(x0 - h) - 10*func(x0) + 18*func(x0 + h) - 6*func(x0 + 2*h) + func(x0 + 3*h)) / (12*h)
    elif type == 'central':
        df = (func(x0 - 2*h) - 8*func(x0 - h) + 8*func(x0 + h) - func(x0 + 2*h)) / (12*h)
    elif type == 'backward1':
        df = (-func(x0 - 3*h) + 6*func(x0 - 2*h) - 18*func(x0 - h) + 10*func(x0) + 3*func(x0 + h)) / (12*h)
    elif type == 'backward2':
        df = (3*func(x0 - 4*h) - 16*func(x0 - 3*h) + 36*func(x0 - 2*h) - 48*func(x0 - h) + 25*func(x0)) / (12*h)
    else:
        raise ValueError("type must be 'forward1', 'forward2', 'backward1', 'backward2' or 'central'")
    return df