#!/bin/bash
if [ $# -ne 1 ]; then
    echo -e "Invalid or Empty arguments.\nSyntax: sh ex.sh /path/to/sarfile"
    exit 1
fi
filepath=${1}
#cpustat
grep "iowait" ${filepath} | head -n 1 |   sed 's/[0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}\ /TS/g' | tr -s ' ' | sed 's/ /,/g' | sed 's/%//g' > /tmp/cpufile.csv
sed -n '/CPU      %usr     %nice      %sys   %iowait/,/Average:        all/p'  ${filepath} |sed '$d' | grep all | sed '$d'| tr -s '[:blank:]' ',' >> /tmp/cpufile.csv

#bandwidth stat
grep -m1 "IFACE" ${filepath} | head -n1 |  sed 's#/##g ; s#%##g' | sed 's/[0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}\ /TS/g' | tr -s '[:blank:]' ',' > /tmp/bwfile.csv
sed -n '/IFACE   rxpck/,/Average:/p' ${filepath} | grep eth0 | sed '$d' | tr -s '[:blank:]' ',' >> /tmp/bwfile.csv

#loadavg
grep -m1 "runq-sz  plist-sz   ldavg-1   ldavg-5  ldavg-15" ${filepath} | head -n1 | sed 's/[0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}\ /TS/g' | tr -s '[:blank:]' ',' > /tmp/loadavg.csv
sed -n '/runq-sz/,/Average:/p' ${filepath} | sed -e '1d' | sed '$d' | sed '$d' | tr -s '[:blank:]' ',' >> /tmp/loadavg.csv

# tps
grep -m1 "tps      rtps      wtps"  ${filepath} | head -n1 |sed 's#/##g' | sed 's/[0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}\ /TS/g' | tr -s '[:blank:]' ',' > /tmp/iotps.csv
sed -n '/tps      rtps      wtps/,/Average:/p'  ${filepath}  | sed -e '1d' | sed '$d' |  sed '$d' | tr -s '[:blank:]' ',' >> /tmp/iotps.csv

#execute py script
/Users/urgensherpa/graphsar/venv/bin/python3 plotter.py
