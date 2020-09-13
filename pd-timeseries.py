import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as dates


df1 = pd.read_csv('sample.csv', index_col='TS', parse_dates=True)
fig, axe = plt.subplots(2, 1)
# df1['rxkBps'].plot(ax=axe[0], figsize=(12, 5))
# df1['txkBps'].plot(ax=axe[1], figsize=(12, 5))

idx = df1.loc['2020-09-13 10:52:01':'2020-09-13 23:59:01'].index
download = df1.loc['2020-09-13 10:52:01':'2020-09-13 23:59:01'].rxkBps
upload = df1.loc['2020-09-13 10:52:01':'2020-09-13 23:59:01'].txkBps
axe[0].plot_date(idx, download, '-')
plt.ylabel('Down KBps')
axe[1].plot_date(idx, upload, '-')
plt.ylabel('Up KBps')
# Label
# axe[0].set_title('Down')
# axe[1].set_title('Up')
axe[0].set(ylabel='Down KBps')
axe[1].set(ylabel='Up KBps')
plt.xlabel('TimeStamp')  # common x label

# locating
axe[0].xaxis.set_major_locator(dates.HourLocator())
axe[0].xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))

axe[1].xaxis.set_major_locator(dates.HourLocator())
axe[1].xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))

# plt.xticks(rotation=45)
plt.tight_layout()
# fig.autofmt_xdate()
plt.show()
