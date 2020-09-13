Requirements
matplotlib==3.3.1
numpy==1.19.1
pandas==1.1.1

sysstat v11.6 or more

1) export system activity file of any particular day.

LC_TIME=C sar -A -t -f /var/log/sysstat/sa14 > /tmp/sar14

2) download the /tmp/sar14

bash ex.sh /path/to/sar14

