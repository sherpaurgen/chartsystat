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

2) download  /tmp/sar14 to your local storage path eg. /home/Johndoe/sar14

3) git clone https://github.com/sherpaurgen/chartsystat 

    3.1 - edit fire.sh with your python path 

    3.2 - chmod +x fire.sh
    
    3.3 - bash fire.sh /home/Johndoe/sar14
    
Execution of fire.sh will generate sys_report.pdf in your script's directory.
you can playaround with sysstat file inside sysstat directory
