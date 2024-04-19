import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义网格大小和步长
N = int(2 / 0.04) + 1
h = 0.04

# 初始化网格
u = [[0 for _ in range(N)] for _ in range(N)]

# 设置边界条件
for i in range(N):
    u[i][0] = 0
    u[i][N-1] = i if i < N/2 else 2 - i
    u[0][i] = 0
    u[N-1][i] = i*(2-i)


# 迭代求解
max_iter = 1000
tolerance = 1e-4
for _ in range(max_iter):
    max_diff = 0.0
    for i in range(1, N-1):
        for j in range(1, N-1):
            new_u = (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1]) / 4.0
            diff = abs(new_u - u[i][j])
            if diff > max_diff:
                max_diff = diff
            u[i][j] = new_u

    if max_diff < tolerance:
        break

# 打印结果
for i in range(N):
    for j in range(N):
        print(u[i][j], end='\t')
    print()

# 创建网格
x = np.linspace(0, 2, N)
y = np.linspace(0, 2, N)
X, Y = np.meshgrid(x, y)

# 将数值解转换为NumPy数组
u = np.array(u)

# 绘制3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, u, cmap='coolwarm')

# 设置坐标轴标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u')

# 设置图形标题
ax.set_title('Numerical Solution')

# 调整坐标轴范围
ax.set_xlim(2, 0)
ax.set_ylim(0, 2)

# 显示图形
plt.show()