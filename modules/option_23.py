#!/usr/bin/python
#
#
import os
import sys
import ansi

header = ansi.escapes.HEADER
blue = ansi.escapes.OKBLUE
green = ansi.escapes.OKGREEN
warning = ansi.escapes.WARNING
fail = ansi.escapes.FAIL
endc = ansi.escapes.ENDC
bold = ansi.escapes.BOLD
underline = ansi.escapes.UNDERLINE

print warning + "\nThis Option Will Change the WiFi HotSpot Password." + endc

cont = raw_input("\n[!]...Press 'Return' to Continue: ")

password = raw_input(warning + "\nEnter a Strong Password for the HotSpot: ") + endc

####################
#Config for Hostapd#
####################

os.system('sudo rm /etc/hostapd/hostapd.conf')

hostapd = """
interface=wlan1
#driver=rtl871xdrv
ssid=Pi_AP
country_code=US
hw_mode=g
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=1
wpa=2
wpa_passphrase=%s
wpa_key_mgmt=WPA-PSK
wpa_pairwise=CCMP
wpa_group_rekey=86400
ieee80211n=1
wme_enabled=1
""" % password

hostapd_path = "/etc/hostapd/hostapd.conf"
hostapd_write = open(hostapd_path, "w")
hostapd_write.write(hostapd)
hostapd_write.close()

print warning + "\n[!]. Restarting 'Hostapd-Sever', Please Wait..." + endc

os.system('sudo service hostapd restart')

print green + "\n[+]. Password Changed" + endc

cont = raw_input(warning + "\n[!]...Press 'Return' to Continue") + endc
