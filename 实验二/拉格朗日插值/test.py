# Description: Lagrange interpolation 测试
import numpy as np
from lagrange import Language

x = np.arange(0, 3.5, 0.5)
y = [0, 0.4794, 0.8415, 0.9975, 0.9093, 0.5985, 0.1411]
x0 = 1.6

f = Language(x, y, x0)
print(f"Interpolation at x0 = {x0}: ", f)