#!/usr/bin/python
#
#
import os
import sys

class bcolors:

    ENDC = '\033[0m'
    RED   = "\033[1;31m"
    GREEN = "\033[0;32m"
    WARNING = "\033[93m"

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
INTERFACES="wlan1"
#INTERFACESv4=""
#INTERFACESv6=""
"""

dhcp_path = "/etc/default/isc-dhcp-server"
dhcp_write = open(dhcp_path, "w")
dhcp_write.write(dhcp_server)
dhcp_write.close()


