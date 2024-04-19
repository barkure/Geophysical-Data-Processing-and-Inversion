# 定义边界条件
def EllTni2Uxl(x, y):
    uxy = 0
    return uxy

def Ellni2Uxr(x, y):
    uxy = y * (2-y)
    return uxy

def Ellni2Uyl(x, y):
    uxy = 0
    return uxy

def Ellni2Uyr(x, y):
    if x < 1:
        uxy = x
    else:
        uxy = 2-x
    return uxy