#!/usr/bin/env python
import os
from datetime import datetime


hostname = '10.42.0.1'
logfile_filename = '/home/mitch/prog/vpn_restart/vpnstatus.log'
ping_response = os.system('/bin/ping -c 1 -t 5 ' + hostname + ' > /dev/null 2>&1')


with open(logfile_filename, 'a') as logfile:
    if ping_response == 0:
        logline = '{0} {1} {2}'.format(str(datetime.now()), hostname, ' is up \n')
        print logline

        logfile.write(str(logline))
        print "log written"  
    else:
        logline = '{0} {1} {2}'.format(str(datetime.now()), hostname, ' is down \n')
        print logline
        logfile.write(str(logline))
        restart_vpn = os.system('/etc/init.d/openvpn restart')
        restartline = '{0} {1}'.format(str(datetime.now()), 'openvpn was restarted \n')
        logfile.write(restartline)     

