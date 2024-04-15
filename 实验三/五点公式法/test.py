# Des
import math
from five_point import FivePoint

x0 = 2
h = 0.001
f = lambda x: math.sin(x)

df1 = FivePoint(f, x0, 'forward1', h)
df2 = FivePoint(f, x0, 'forward2', h)
df3 = FivePoint(f, x0, 'backward1', h)
df4 = FivePoint(f, x0, 'backward2', h)
df5 = FivePoint(f, x0, 'central', h)
print("forward1:", df1)
print("forward2:", df2)
print("backward1:", df3)
print("backward2:", df4)
print("central:", df5)