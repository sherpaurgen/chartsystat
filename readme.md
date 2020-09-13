Python package requirements:-
    matplotlib==3.3.1
    numpy==1.19.1
    pandas==1.1.1

Linux/Unix package requiremnts:-
    -sysstat v11.6 or more
    -sed
    -tr

1) export system activity file of any particular day.

    LC_TIME=C sar -A -t -f /var/log/sysstat/sa14 > /tmp/sar14

2) download the /tmp/sar14
3) edit fire.sh with your python path 
4) chmod +x fire.sh
    bash fire.sh /path/to/sar14
    
    execution of script will generate sys_report.pdf in your script's directory.
    you can play with sysstat file - sar13 from 48core, 125G memory system.

