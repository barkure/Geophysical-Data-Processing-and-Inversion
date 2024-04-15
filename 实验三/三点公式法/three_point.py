# Description: 三点公式法

def ThreePoint(func, x0, type, h):
    if type == 'forward':
        df = (-3*func(x0) + 4*func(x0 + h) - func(x0 + 2*h)) / (2*h)
    elif type == 'backward':
        df = (3*func(x0) - 4*func(x0 - h) + func(x0 - 2*h)) / (2*h)
    elif type == 'central':
        df = (func(x0 + h) - func(x0 - h)) / (2*h)
    else:
        raise ValueError("type must be 'forward', 'backward' or 'central'")
    return df