import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values,y_values,c = y_values,edgecolors='none',s=40,cmap=plt.cm.Reds)

plt.show()