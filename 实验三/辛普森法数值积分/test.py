# Description: 辛普森法数值积分测试
from simpson import intsimpson
import sympy as sp

x = sp.symbols('x')
# 定义被积函数为正弦函数
f_expr = sp.sin(x)

types = ['simpson', '3/8', 'composite_simpson']
for type in types:
    [q, step] = intsimpson(f_expr, 0, 10, type, 1e-4)
    print(f'使用{type}方法计算积分：')
    print(f'积分的近似值是: {q.evalf()}')
    print(f'使用的步数是: {step}')
    print('-' * 50)
