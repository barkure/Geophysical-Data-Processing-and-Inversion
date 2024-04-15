# Description: Newton interpolation 测试
from newton import Newton
import numpy as np

x = np.arange(1, 7, 1)
y = [0, 0.6931, 1.0986, 1.3863, 1.6094, 1.7918]
x0 = 1.5

f = Newton(x, y, x0)
print(f"Interpolation at x0 = {x0}: ", f)