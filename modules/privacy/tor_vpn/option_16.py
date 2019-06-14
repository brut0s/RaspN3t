#!/usr/bin/python
#
#
import os,sys

class bcolors:

    ENDC = '\033[0m'
    RED   = "\033[1;31m"
    GREEN = "\033[0;32m"
    WARNING = "\033[93m"

print bcolors.WARNING + "\nThis Configuration Will turn your Raspberry-Pi into a Ethernet to Tor+VPN Router" + bcolors.ENDC

cont = raw_input("\n[!]...Press 'Return' to Continue: ")

#import config.eth0_dhcp

os.system('sudo ifconfig eth0 192.168.42.1')

print bcolors.WARNING + "\n[!]. FLUSHING CURRENT IP-TABLES" + bcolors.ENDC

os.system('sudo iptables -F && sudo iptables -t nat -F')

print bcolors.GREEN + "\n[+]. Iptables are Flushed" + bcolors.ENDC

print bcolors.WARNING + "\n[+]. Configuring IP-Tables, please Wait..." + bcolors.ENDC

os.system('sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE')
os.system('sudo iptables -A FORWARD -i wlan1 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT')
os.system('sudo iptables -A FORWARD -i eth0 -o wlan1 -j ACCEPT')
os.system('sudo sh -c "iptables-save > /etc/iptables/rules.v4"')
os.system('sudo update-rc.d tor disable')

print bcolors.GREEN + "\n[+]. Iptables are Reconfigured" + bcolors.ENDC

print bcolors.WARNING + "\n[+]. Enabling Tor at boot and Disabling Hostapd at boot" + bcolors.ENDC

os.system('sudo service tor start')
os.system('sudo update-rc.d hostapd disable')
os.system('sudo update-rc.d tor enable') 

print bcolors.GREEN + "\n[+]. Configuration Complete" + bcolors.ENDC

cont = raw_input("\n[!]...Press 'Return' to Continue: ")
