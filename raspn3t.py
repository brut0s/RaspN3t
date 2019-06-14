#!/usr/bin/python
#
#
import os
import sys
import modules.ansi

ansi = modules.ansi
header = ansi.escapes.HEADER
blue = ansi.escapes.OKBLUE
green = ansi.escapes.OKGREEN
warning = ansi.escapes.WARNING
fail = ansi.escapes.FAIL
endc = ansi.escapes.ENDC
bold = ansi.escapes.BOLD
underline = ansi.escapes.UNDERLINE

print """

Welcome to


  .;'                     `;,
 .;'  ,;'             `;,  `;,
.;'  ,;'  ,;'  _  `;,  `;,  `;,
::   ::   :   ( )   :   ::   ::
':.  ':.  ':. /_\ ,:'  ,:'  ,:'
 ':.  ':.    /___\    ,:'  ,:'
  ':.       /     \       '

 ____                 _   _ _____ _
|  _ \ __ _ ___ _ __ | \ | |___ /| |_
| |_) / _` / __| '_ \|  \| | |_ \| __|
|  _ < (_| \__ \ |_) | |\  |___) | |_
|_| \_\__,_|___/ .__/|_| \_|____/ \__|
               |_|

The Official Automated Network-Adapter
                for
                the
           Raspberry-Pi 3
     https://github.com/brut0s
	    contributors
     https://github.com/TheCryptek
"""
def print_menu():

    print "\n###############################################################"
    print "Standard Configurations"
    print "###############################################################"
    print warning + "\n[01]. Ethernet to WiFi Adapter"
    print "[02]. Wireless to Ethernet adapter"
    print "[03]. WiFi Repeater"
    print "[04]. USB-Tethering to WiFi Adapter"
    print "[05]. USB-Tethering to Ethernet Adapter" + endc
    print "\n###############################################################"
    print "Configurations for Privacy and Anonymity"
    print "###############################################################"
    print warning + "\n[06]. Ethernet to Tor Router"
    print "[07]. Wireless to Ethernet with Tor"
    print "[08]. WiFi Repeater with Tor"
    print "[09]. USB-Tethering to WiFi Adapter with Tor"
    print "[10]. USB-Tethering to Ethernet Adapter with Tor"
    print "[11]. Ethernet to VPN Router"
    print "[12]. Wireless to Ethernet with VPN"
    print "[13]. WiFi Repeater with VPN"
    print "[14]. USB-Tethering to WiFi Adapter with VPN"
    print "[15]. USB-Tethering to Ethernet Adapter with VPN"
    print "[16]. Ethernet to Tor+VPN Router"
    print "[17]. Wireless to Ethernet with Tor+VPN"
    print "[18]. WiFi Repeater with Tor+VPN"
    print "[19]. USB-Tethering to WiFi Adapter with Tor+VPN"
    print "[20]. USB-Tethering to Ethernet Adapter with Tor+VPN"
    print "[21]. Change VPN" + endc
    print "\n###############################################################"
    print "Network Settings"
    print "###############################################################"
    print warning + "\n[22]. View Sample of wpa_supplicant Config File"
    print "[23]. Change Wifi Password"
    print "[24]. Connect to a Wireless Network"
    print "[25]. Check for Updates"
    print "[26]. Exit" + endc
    print "\n-------------"
    print fail + "Version 1.0.5" + endc
    print "-------------"

loop=True

while loop:
    print_menu()
    choice = input(warning + "\n[!]. Select an Option [1-26]: " + endc)

    if choice==1:	#STANDARD#

	import modules.standard.option_1
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==2:

	print warning + "\nFirst Lets get the Raspberry Pi Online" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.wifi.wireless_setup
	import modules.standard.option_2
      	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==3:

	print warning + "\nFirst Lets get the Raspberry Pi Online" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.wifi.wireless_setup
	import modules.standard.option_3
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==4:

	print warning + "\nFirst Plug in your Phone with USB-Tethering enabled" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.standard.option_4
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==5:

	print warning + "\nFirst Plug in your Phone with USB-Tethering enabled" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
	import modules.standard.option_5
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==6:	#PRIVACY#

	import modules.privacy.tor.option_6
      	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==7:

	print warning + "\nFirst Lets get the Raspberry Pi Online" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.wifi.wireless_setup	
	#import modules.config.hotspot_dhcp
	#print warning + "\nFirst Lets get the Raspberry Pi Online" + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #import modules.wifi.wireless_setup
	import modules.privacy.tor.option_7
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==8:

	print warning + "\nFirst Lets get the Raspberry Pi Online" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.wifi.wireless_setup
	import modules.privacy.tor.option_8
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==9:

	print warning + "\nFirst Plug in your Phone with USB-Tethering enabled" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.privacy.tor.option_9
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==10:

	print warning + "\nFirst Plug in your Phone with USB-Tethering enabled" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.privacy.tor.option_10
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==11:

	import modules.privacy.vpn.option_11
      	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==12:

	print warning + "\nFirst Lets get the Raspberry Pi Online" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.wifi.wireless_setup
	import modules.vpn.option_12
      	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==13:

	print warning + "\nFirst Lets get the Raspberry Pi Online" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.wifi.wireless_setup
	import modules.privacy.vpn.option_13
      	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==14:

	print warning + "\nFirst Plug in your Phone with USB-Tethering enabled" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.privacy.vpn.option_14
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==15:

	print warning + "\nFirst Plug in your Phone with USB-Tethering enabled" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.privacy.vpn.option_15
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==16:

	import modules.privacy.tor_vpn.option_16
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==17:

	print warning + "\nFirst Lets get the Raspberry Pi Online" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.wifi.wireless_setup
	import modules.privacy.tor_vpn.option_17
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==18:

	print warning + "\nFirst Lets get the Raspberry Pi Online" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.wifi.wireless_setup
	import modules.privacy.tor_vpn.option_18
      	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==19:

	print warning + "\nFirst Plug in your Phone with USB-Tethering enabled" + endc
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        import modules.privacy.tor_vpn.option_19
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==20:

	print warning + "\nFirst Plug in your Phone with USB-Tethering enabled" + endc	
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
	import modules.privacy.tor_vpn.option_20
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==21:	#CHANGE VPN#

        import modules.privacy.vpn.vpn_menu

    elif choice==22:	#WPA_SUPPLICANT SAMPLE#

	import modules.wifi.wpa_supplicant
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")

    elif choice==23:	#CHANGE WiFi PASSWORD#

        import modules.option_23

    elif choice==24:	#CONNECT TO WIRELESS NETWORK#

        import modules.wifi.wireless_setup
	#print warning + "\n[!]. Rebooting For Changes to Take Effect." + endc
        #cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        #os.system("sudo reboot now")

    elif choice==25:	#UPDATE RASPN3T VIA GIT PULL#

        import modules.update

    elif choice==26:	#EXIT#

        print green + "\nThanks for using RaspN3t" + endc
        loop=False

    else:

        raw_input(fail + "\n[!]-Error That was a invalid Number, \n\nSelect from [1-26]" + endc)
