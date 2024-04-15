
from simpson import IntSimpson
import math


f = lambda x: math.sin(x)
a = 0
b = 10
eps = 1e-6

I, step = IntSimpson(f, a, b, 'simpson', eps)
print(I, step)
I, step = IntSimpson(f, a, b, 'simpson_3_8', eps)
print(I, step)

