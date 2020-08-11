# 静态图表matplotlib

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, linewidth=5) #折线图
plt.scatter(x, y, s=200) #散点图

plt.title("Square Numbers", fontsize=24) #图表标题
plt.xlabel("Value", fontsize=14) #x轴标题
plt.ylabel("Square of Value", fontsize=14) #y轴标题

plt.show() #显示图像
plt.savefig(r'E:\Temp\数据可视化\squares_plot.png')  #保存图像
```



# 动态图表Pygal

```python
import pygal

frequencies = [155, 167, 168, 170, 159, 181]

hist = pygal.Bar() #直方图
hist.add('D6', frequencies)

hist.title = "Results of rolling one D6 1,000 times."
hist.x_labels = [ '1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.render_to_file(r'E:\Temp\数据可视化\die_visual.svg')
```



# 文件格式CSV和JSON

```python
import csv
filename = r'E:\sth.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # do sth

import json
filename = r'E:\sth.json'
with open(filename) as f:
    pop_data = json.load(f)
    # do sth
```



# requests使用API

```python
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()
print(response_dict.keys())
# do sth
```



# 其他

```python
from datetime import datetime

dates = []
dates.append(datetime.strptime(row[0], '%Y/%m/%d'))
```

