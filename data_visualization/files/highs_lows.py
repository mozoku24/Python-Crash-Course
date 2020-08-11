import csv
from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获取日期、最高气温和最低气温
filename = r'E:\Temp\数据可视化\data\sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[2], '%Y/%m/%d'))
        highs.append(int(row[8]))
        lows.append(int(row[9]))
        
#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#设置图形的格式
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate() #绘制斜的日期标签
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
