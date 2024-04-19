# Description: 第二类边界条件三次样条插值测试
from cubic_spline_2 import cubic_spline_2
import numpy as np

# 测试数据
x = np.arange(1, 9, 1)
y = np.array([0.8415, 0.9093, 0.1411, -0.7568, -0.9589, -0.2794, 0.6570, 0.9894])

y_1 = -0.8415 # 左端点的一阶导数值
y_N = -0.9894 # 右端点的一阶导数值
x0 = 4.3 # 插值点

f, f0 = cubic_spline_2(x, y, y_1, y_N, x0)
print(f"Interpolation function at {x0}: \n", f)
print('-' * 80)
print(f"Interpolation value at {x0}: ", f0)
