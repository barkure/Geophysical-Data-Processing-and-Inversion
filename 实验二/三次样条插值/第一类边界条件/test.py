# Description: 第一类边界条件三次样条插值测试
import numpy as np
from cubic_spline_1 import cubic_spline_1


# 测试数据
x = np.arange(1, 9, 1)
y = np.array([0.8415, 0.9093, 0.1411, -0.7568, -0.9589, -0.2794, 0.6570, 0.9894])

y_1 = 0.5403 # 左端点的一阶导数值
y_N = -0.1455 # 右端点的一阶导数值
x0 = 4.3 # 插值点

f, f0 = cubic_spline_1(x, y, y_1, y_N, x0)
print(f"Interpoloation function at {x0}: \n", f)
print('-' * 80)
print(f"Interpoloation value at {x0}: ", f0)
