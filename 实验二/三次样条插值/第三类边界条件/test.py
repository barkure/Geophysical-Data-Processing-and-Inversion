# Description: 第三类边界条件三次样条插值测试
import numpy as np
from cubic_spline_3 import cubic_spline_3

x = np.array([0, 1, 2, 3, 4, 5, 6.2832])
y = np.array([0, 0.8415, 0.9093, 0.1411, -0.7568, -0.9589, 0])
f, f0 = cubic_spline_3(x, y, 4.3)

print('-' * 80)
print(f"Interpolation value at 4.3: ", f0)