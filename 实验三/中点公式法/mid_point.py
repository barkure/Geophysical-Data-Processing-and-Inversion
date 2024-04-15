# Description: 中点公式法

def MidPoint(func, x0, h):
    df = (func(x0 + h) - func(x0 - h)) / (2 * h)
    return df