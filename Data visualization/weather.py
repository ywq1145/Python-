import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs, dates, lows = [], [], []
    for row in reader:
        low = int(row[2])
        high = int(row[1])
        lows.append(low)
        highs.append(high)
        date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(date)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red',alpha = 0.5)
    plt.plot(dates, lows, c='blue',alpha = 0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.title("Daily high temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)

    # 设置日期格式为Jan 2014
    date_format = plt.matplotlib.dates.DateFormatter('%b %Y')
    plt.gca().xaxis.set_major_formatter(date_format)

    # 设置主要刻度线为每个月
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
