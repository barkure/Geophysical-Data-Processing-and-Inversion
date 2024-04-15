# Description: 复合梯形公式法测试
from combine_traprl import CombineTraprl


eps = 1e-6
a = 2
b = 4
f = lambda x: 1/(x**2 - 1)

I, n = CombineTraprl(f, a, b, eps)
print(f"Integral: {I}")
print(f"Steps: {n}")