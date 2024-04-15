# Description: 三点公式法测试
import math
from three_point import ThreePoint

x0 = 2
h = 0.1
f = lambda x: math.sin(x)

df1 = ThreePoint(f, x0, 'forward', h)
df2 = ThreePoint(f, x0, 'backward', h)
df3 = ThreePoint(f, x0, 'central', h)
print("forward:", df1)
print("backward:", df2)
print("central:", df3)