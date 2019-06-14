#!/usr/bin/python
#
#

print """
####################################
# Sample Config for wpa_supplicant #
#                                  #
#        Path to Config:           #
#/etc/wpa_supplicant/wpa_supplicant#
####################################
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

# Example Open

network={
    ssid=""
    scan_ssid=1
    key_mgmt=NONE
}



# Example WEP

network={
    ssid=""
    scan_ssid=1
    key_mgmt=NONE
    wep_key0=""
}



# Example WPA

network={
    ssid=""
    scan_ssid=1
    key_mgmt=WPA-PSK
    psk=""
}



# Example WPA2

network={
    ssid=""
    scan_ssid=1
    proto=RSN
    key_mgmt=WPA-PSK
    psk=""
}

"""
