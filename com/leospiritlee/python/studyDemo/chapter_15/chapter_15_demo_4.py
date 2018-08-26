import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, c='red',edgecolors='none', s=40)
plt.scatter(x_values, y_values, c=(0,0,0.8),edgecolors='none', s=40)

plt.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Blues, edgecolors='none',s=40)

#  设置坐标轴取值范围
plt.axis([0,1100,0,1100000])



# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')