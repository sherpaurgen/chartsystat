import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.style as style

df1 = pd.read_csv('/tmp/bwfile.csv', index_col='TS', parse_dates=True)
df2 = pd.read_csv('/tmp/cpufile.csv', index_col='TS', parse_dates=True)
df3 = pd.read_csv('/tmp/loadavg.csv', index_col='TS', parse_dates=True)
df4 = pd.read_csv('/tmp/iotps.csv', index_col='TS', parse_dates=True)

fig, axe = plt.subplots(6, 1, figsize=(20, 15))
style.use('fivethirtyeight')

# df1['rxkBps'].plot(ax=axe[0], figsize=(12, 5))
# df1['txkBps'].plot(ax=axe[1], figsize=(12, 5))

# idx = df1.loc['2020-09-13 10:52:01':'2020-09-13 23:59:01'].index
# download = df1.loc['2020-09-13 10:52:01':'2020-09-13 23:59:01'].rxkBs
# upload = df1.loc['2020-09-13 10:52:01':'2020-09-13 23:59:01'].txkBs

# receive kbps
axe[0].plot_date(df1.index, df1['rxkBs'], '-', linewidth=0.5)
# upload kbps
axe[1].plot_date(df1.index, df1['txkBs'], '--', linewidth=0.5)

# cpu stats
axe[2].plot_date(df2.index, df2['iowait'], '--',
                 linewidth=0.5, color='red', label='iowait%')
axe[2].plot_date(df2.index, df2['usr'], '--', linewidth=0.7, color="#6c3376",
                 label='usr%')
axe[2].plot_date(df2.index, df2['sys'], '--', linewidth=0.8, color='orange',
                 label='sys%')
axe[2].legend(loc=2, fontsize=7)

# loadavg
axe[3].plot_date(df3.index, df3['ldavg-1'], '--',
                 linewidth=0.5, color='red', label='ldavg-1')
axe[3].plot_date(df3.index, df3['ldavg-5'], '--',
                 linewidth=0.5, color='green', label='ldavg-5')
axe[3].plot_date(df3.index, df3['ldavg-15'], '--',
                 linewidth=0.5, color='blue', label='ldavg-15')
axe[3].legend(loc=2, fontsize=7)

# blocked tasks
axe[4].plot_date(df3.index, df3['blocked'], '--',
                 linewidth=0.5, color='red', label='blockedTasks')
axe[4].plot_date(df3.index, df3['runq-sz'], '--',
                 linewidth=0.5, color='blue', label='runq-sz')
axe[4].legend(loc=2, fontsize=7)

# iops TPS
axe[5].plot_date(df4.index, df4['tps'], '--', linewidth=0.5,
                 color='#BB8FCE', label='tps')
axe[5].plot_date(df4.index, df4['rtps'], '-', linewidth=0.5,
                 color='#78281F', label='rtps')
axe[5].plot_date(df4.index, df4['wtps'], '-', linewidth=0.5,
                 color='#D4AC0D', label='wtps')
axe[5].legend(loc=2, fontsize=7)

# Label
# axe[0].set_title('Down')
# axe[1].set_title('Up')
axe[0].set_ylabel('Down KBps', fontsize=7)
axe[1].set_ylabel('Up KBps', fontsize=7)
axe[2].set_ylabel('Wait%', fontsize=7)
axe[3].set_ylabel('Loadavg', fontsize=7)
axe[4].set_ylabel('Blocked', fontsize=7)
axe[5].set_ylabel('tps', fontsize=7)
plt.xlabel('TimeStamp', fontsize=7)  # common x label

# locating axis major tick
axe[0].xaxis.set_major_locator(dates.MinuteLocator(interval=30))
axe[0].xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))


axe[1].xaxis.set_major_locator(dates.MinuteLocator(interval=30))
axe[1].xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))

axe[2].xaxis.set_major_locator(dates.MinuteLocator(interval=30))
axe[2].xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))

axe[3].xaxis.set_major_locator(dates.MinuteLocator(interval=30))
axe[3].xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))

axe[4].xaxis.set_major_locator(dates.MinuteLocator(interval=30))
axe[4].xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))

axe[5].xaxis.set_major_locator(dates.MinuteLocator(interval=30))
axe[5].xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))

plt.xticks(rotation=45)
plt.tight_layout()
# fig.autofmt_xdate()
plt.setp(axe[0].xaxis.get_majorticklabels(), rotation=45, fontsize=7)
plt.setp(axe[1].xaxis.get_majorticklabels(), rotation=45, fontsize=7)
plt.setp(axe[2].xaxis.get_majorticklabels(), rotation=45, fontsize=7)
plt.setp(axe[3].xaxis.get_majorticklabels(), rotation=45, fontsize=7)
plt.setp(axe[4].xaxis.get_majorticklabels(), rotation=45, fontsize=7)
plt.setp(axe[5].xaxis.get_majorticklabels(), rotation=45, fontsize=7)


plt.setp(axe[0].yaxis.get_majorticklabels(), fontsize=7)
plt.setp(axe[1].yaxis.get_majorticklabels(), fontsize=7)
plt.setp(axe[2].yaxis.get_majorticklabels(), fontsize=7)
plt.setp(axe[3].yaxis.get_majorticklabels(), fontsize=7)
plt.setp(axe[4].yaxis.get_majorticklabels(), fontsize=7)
plt.setp(axe[5].yaxis.get_majorticklabels(), fontsize=7)

plt.savefig('sys_report.pdf')
# plt.show()
