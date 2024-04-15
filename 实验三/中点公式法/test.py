# Description: 中点公式法测试
from mid_point import MidPoint
import math

x0 = 4
h = 0.01
f = lambda x: math.sqrt(x)

df = MidPoint(f, x0, h)
print(f"diterative at x = {x0} (h = {h}) is", df)

