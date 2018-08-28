import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk_v2()

# 设置绘图窗口尺寸
plt.figure(dpi=128,figsize=(10,6))

point_numbers = list(range(rw.num_points))

plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none',s=1)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.scatter(0,0, c='red',edgecolors='none',s=15)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='green',edgecolors='none',s=15)


# plt.show()

pic_name = 'squares_plot_1.png'
plt.savefig(pic_name, bbox_inches='tight')
