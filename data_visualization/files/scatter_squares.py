import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
#plt.scatter(x_values, y_values, c=(0,0,0.8), edgecolor='none', s=40) 
#c颜色例如'red'或者RGB，s点的尺寸
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
#c颜色设置成一个列表，cmap用什么颜色映射（浅蓝色->深蓝色）

#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

#plt.show() #显示图片
#plt.savefig('squres_plot.png', bbox_inches='tight') #保存到notepad++的目录下
plt.savefig(r'E:\Temp\数据可视化\squares_plot.png', bbox_inches='tight') 
#bbox_inches将图标多余空白裁减掉