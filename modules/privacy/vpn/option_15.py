#!/usr/bin/python
#
#
import os,sys

class bcolors:

    ENDC = '\033[0m'
    RED   = "\033[1;31m"
    GREEN = "\033[0;32m"
    WARNING = "\033[93m"

print bcolors.WARNING + "\nThis Configuration Will turn your Raspberry-Pi into a Ethernet Adapter with VPN using USB-Tethering." + bcolors.ENDC

cont = raw_input("\n[!]...Press 'Return' to Continue: ")

outlet = raw_input(bcolors.WARNING + "\n[!]. Enter The Wireless Interface to use as the HotSpot: " + bcolors.ENDC)


############################
#Config for isc-dhcp-server#
############################

os.system('sudo rm /etc/default/isc-dhcp-server')

dhcp_server = """
# Defaults for isc-dhcp-server initscript
# sourced by /etc/init.d/isc-dhcp-server
# installed at /etc/default/isc-dhcp-server by the maintainer scripts

#
# This is a POSIX shell fragment
#

# Path to dhcpd's config file (default: /etc/dhcp/dhcpd.conf).
#DHCPD_CONF=/etc/dhcp/dhcpd.conf

# Path to dhcpd's PID file (default: /var/run/dhcpd.pid).
#DHCPD_PID=/var/run/dhcpd.pid

# Additional options to start dhcpd with.
#	Don't use options -cf or -pf here; use DHCPD_CONF/ DHCPD_PID instead
#OPTIONS=""

# On what interfaces should the DHCP server (dhcpd) serve DHCP requests?
#	Separate multiple interfaces with spaces, e.g. "eth0 eth1".
INTERFACES="%s"
#INTERFACESv4=""
#INTERFACESv6=""
""" % outlet

dhcp_path = "/etc/default/isc-dhcp-server"
dhcp_write = open(dhcp_path, "w")
dhcp_write.write(dhcp_server)
dhcp_write.close()




####################
#Config for Hostapd#
####################

os.system('sudo rm /etc/hostapd/hostapd.conf')

hostapd = """
interface=%s
#driver=rtl871xdrv
ssid=RaspN3t
country_code=US
hw_mode=g
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=Raspberry-AP
wpa_key_mgmt=WPA-PSK
wpa_pairwise=CCMP
wpa_group_rekey=86400
ieee80211n=1
wme_enabled=1
""" % outlet

hostapd_path = "/etc/hostapd/hostapd.conf"
hostapd_write = open(hostapd_path, "w")
hostapd_write.write(hostapd)
hostapd_write.close()


###############################
#Config for Network Interfaces#
###############################

os.system('sudo rm /etc/network/interfaces')

interfaces = """
# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d


auto lo
iface lo inet loopback


# eth0

allow-hotplug eth0
auto eth0
iface eth0 inet dhcp


# usb0

iface usb0 inet dhcp


allow-hotplug %s
auto %s
iface %s inet static
  post-up /usr/sbin/hostapd -B /etc/hostapd/hostapd.conf
  #post-up service isc-dhcp-server restart
  address 192.168.42.1
  netmask 255.255.255.0

""" % (outlet,outlet,outlet,inlet,inlet,inlet)

interfaces_path = "/etc/network/interfaces"
interfaces_write = open(interfaces_path, "w")
interfaces_write.write(interfaces)
interfaces_write.close()

print bcolors.WARNING + "\n[!]. FLUSHING CURRENT IP-TABLES""" + bcolors.ENDC

os.system('sudo iptables -F && sudo iptables -t nat -F')

print bcolors.GREEN + "\n[+]. Iptables are Flushed" + bcolors.ENDC

print bcolors.WARNING + "\n[!]. Configuring IP-Tables, please Wait..." + bcolors.ENDC

os.system('sudo iptables -t nat -A POSTROUTING -o  ' + outlet + ' -j MASQUERADE')
os.system('sudo iptables -A FORWARD -i usb0 -o  ' + outlet + ' -m state --state RELATED,ESTABLISHED -j ACCEPT')
os.system('sudo iptables -A FORWARD -i usb0 ' + ' -o  ' + outlet + ' -j ACCEPT')
os.system('sudo sh -c "iptables-save > /etc/iptables/rules.v4"')

print bcolors.GREEN + "\n[+]. Iptables are Reconfigured" + bcolors.ENDC

print bcolors.WARNING + "\n[!]. Disabling Tor at boot." + bcolors.ENDC

os.system('sudo service tor stop')
os.system('sudo update-rc.d tor disable')

print bcolors.WARNING + "\n[!]. Restarting DHCP-Server." + bcolors.ENDC

os.system('sudo service isc-dhcp-server restart')

print bcolors.GREEN + "\n[+]. Configuration Complete" + bcolors.ENDC

cont = raw_input("\n[!]...Press 'Return' to Continue: ")
