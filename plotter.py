import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.style as style

dfbw = pd.read_csv('/tmp/bwfile.csv', index_col='TS', parse_dates=True)
dfcpu = pd.read_csv('/tmp/cpufile.csv', index_col='TS', parse_dates=True)
dfloadavg = pd.read_csv('/tmp/loadavg.csv', index_col='TS', parse_dates=True)
dfiops = pd.read_csv('/tmp/iotps.csv', index_col='TS', parse_dates=True)

fig, axe = plt.subplots(6, 1, figsize=(20, 15))
style.use('fivethirtyeight')
# receive kbps
axe[0].plot_date(dfbw.index, dfbw['rxkBs'], '-', linewidth=0.5)
# upload kbps
axe[1].plot_date(dfbw.index, dfbw['txkBs'], '--', linewidth=0.5)

# cpu stats
axe[2].plot_date(dfcpu.index, dfcpu['iowait'], '--',
                 linewidth=0.5, color='red', label='iowait%')
axe[2].plot_date(dfcpu.index, dfcpu['usr'], '--', linewidth=0.7, color="#6c3376",
                 label='usr%')
axe[2].plot_date(dfcpu.index, dfcpu['sys'], '--', linewidth=0.8, color='orange',
                 label='sys%')
axe[2].legend(loc=2, fontsize=7)

# loadavg
axe[3].plot_date(dfloadavg.index, dfloadavg['ldavg-1'], '--',
                 linewidth=0.5, color='red', label='ldavg-1')
axe[3].plot_date(dfloadavg.index, dfloadavg['ldavg-5'], '--',
                 linewidth=0.5, color='green', label='ldavg-5')
axe[3].plot_date(dfloadavg.index, dfloadavg['ldavg-15'], '--',
                 linewidth=0.5, color='blue', label='ldavg-15')
axe[3].legend(loc=2, fontsize=7)

# blocked tasks
axe[4].plot_date(dfloadavg.index, dfloadavg['blocked'], '--',
                 linewidth=0.5, color='red', label='blockedTasks')
axe[4].plot_date(dfloadavg.index, dfloadavg['runq-sz'], '--',
                 linewidth=0.5, color='blue', label='runq-sz')
axe[4].legend(loc=2, fontsize=7)

# iops TPS
axe[5].plot_date(dfiops.index, dfiops['tps'], '--', linewidth=0.7,
                 color='red', label='tps')
axe[5].plot_date(dfiops.index, dfiops['rtps'], '-', linewidth=0.5,
                 color='green', label='rtps')
axe[5].plot_date(dfiops.index, dfiops['wtps'], '-', linewidth=0.5,
                 color='blue', label='wtps')
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
for ax in axe:
    ax.xaxis.set_major_locator(dates.MinuteLocator(interval=30))
    ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))

plt.xticks(rotation=45)
plt.tight_layout()
# fig.autofmt_xdate()
for ax in axe:
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, fontsize=7)
    plt.setp(ax.yaxis.get_majorticklabels(), fontsize=7)

plt.savefig('sys_report.pdf')
# plt.show()

