#!/usr/bin/python
#
#
import os,sys

class bcolors:

    ENDC = '\033[0m'
    RED   = "\033[1;31m"
    GREEN = "\033[0;32m"
    WARNING = "\033[93m"

print bcolors.WARNING + "\nThis Configuration Will turn your Raspberry-Pi into a WiFi Repeater with VPN" + bcolors.ENDC

cont = raw_input("\n[!]...Press 'Return' to Continue: ")

#import config.hotspot_dhcp

print bcolors.WARNING + "\n[!]. FLUSHING CURRENT IP-TABLES""" + bcolors.ENDC

os.system('sudo iptables -F && sudo iptables -t nat -F')

print bcolors.GREEN + "\n[+]. Iptables are Flushed" + bcolors.ENDC

print bcolors.WARNING + "\n[+]. Configuring IP-Tables, please Wait..." + bcolors.ENDC

os.system('sudo iptables -t nat -A PREROUTING -i wlan1 -p tcp --dport 22 -j REDIRECT --to-ports 22')
os.system('sudo iptables -t nat -A PREROUTING -i wlan1 -p udp --dport 53 -j REDIRECT --to-ports 53')
os.system('sudo iptables -t nat -A PREROUTING -i wlan1 -p tcp --syn -j REDIRECT --to-ports 9040')
os.system('sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"')

print bcolors.GREEN + "\n[+]. Iptables are Reconfigured" + bcolors.ENDC

print bcolors.WARNING + "\nEnabling Tor, Hostapd to run at boot" + bcolors.ENDC
 
os.system('sudo service tor start')
os.system('sudo update-rc.d hostapd enable')
os.system('sudo update-rc.d tor enable') 

print bcolors.GREEN + "\n[+]. Configuration Complete" + bcolors.ENDC

cont = raw_input("\n[!]...Press 'Return' to Continue: ")


