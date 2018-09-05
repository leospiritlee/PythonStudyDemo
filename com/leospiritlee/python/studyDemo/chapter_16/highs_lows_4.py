from datetime import datetime
import csv
from matplotlib import pyplot as plt

# %A    星期 用单词表示
# %B    月份 用单词表示
# %m    用数字表示的月份
# %d    用数字表示月份的一天
# %Y    四位数字的年份
# %y    两位数字的年份
# %H    24小时制
# %I    12小时制
# %p    am 或 pm
# %M    分钟数 （00～59）
# %S    秒数 （00～61）

file_name = 'sitka_weather_2014.csv'
with open(file_name) as f:
    reader = csv.reader(f)

    header_row = next(reader)

    dates, highs, lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)


    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red', alpha=0.5)
    plt.plot(dates,lows,c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue',alpha=0.1)

    plt.title('Daily high and low temperatures, 2014', fontsize =24)

    plt.xlabel('',fontsize =16)

    fig.autofmt_xdate()

    plt.ylabel('Temperature(F)', fontsize =16)

    plt.tick_params(axis='both', which= 'major', labelsize=16)

    plt.show()


