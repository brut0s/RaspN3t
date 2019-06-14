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

def print_menu():

    print "\n###############################################################"
    print "Free-VPN.com"
    print "###############################################################"
    print bcolors.WARNING + "\n[01]. FreeVPN.be-TCP443"
    print "[02]. FreeVPN.be-TCP80"
    print "[03]. FreeVPN.be-UDP-40000"
    print "[04]. FreeVPN.be-UDP-53"
    print "[05]. FreeVPN.co,uk-TCP443"
    print "[06]. FreeVPN.co.uk-TCP80"
    print "[07]. FreeVPN.co.uk-UDP-40000"
    print "[08]. FreeVPN.co.uk-UDP-53"
    print "[09]. FreeVPN.im-TCP443"
    print "[10]. FreeVPN.im-TCP443"
    print "[11]. FreeVPN.im-TCP80"
    print "[12]. FreeVPN.im-UDP-40000"
    print "[13]. FreeVPN.im-UDP-53"
    print "[14]. FreeVPN.it-TCP443"
    print "[15]. FreeVPN.it-TCP80"
    print "[16]. FreeVPN.it-UDP-40000"
    print "[17]. FreeVPN.it-UDP-53"
    print "[18]. FreeVPN.me-TCP443"
    print "[19]. FreeVPN.me-TCP80"
    print "[20]. FreeVPN.me-UDP-40000"
    print "[21]. FreeVPN.me-UDP-53"
    print "[22]. FreeVPN.se-TCP443"
    print "[23]. FreeVPN.se-TCP80"
    print "[24]. FreeVPN.se-UDP-40000"
    print "[25]. FreeVPN.se-UDP-53"+ bcolors.ENDC
    print "\n###############################################################"
    print "VPN-Book.com"
    print "###############################################################"
    print bcolors.WARNING + "\n[26]. vpnbook-euro1-tcp443"
    print "[27]. vpnbook-euro1-tcp80"
    print "[28]. vpnbook-euro1-udp25000"
    print "[29]. vpnbook-euro1-udp53"
    print "[30]. vpnbook-euro2-tcp443"
    print "[31]. vpnbook-euro2-tcp80"
    print "[32]. vpnbook-euro2-udp25000"
    print "[33]. vpnbook-euro2-udp53"+ bcolors.ENDC
    print "\n###############################################################"
    print "Custom VPN Settings"
    print "###############################################################"
    print bcolors.WARNING + "\n[34]. View Sample for Configuring wpa_supplicant"
    print "[35]. Change Wifi Password"
    print "[36]. Connect to a Wireless Network"
    print "[37]. Check for Updates"
    print "[38]. Exit" + bcolors.ENDC

loop=True

while loop:
    print_menu()
    choice = input(bcolors.WARNING + "\n[!]. Select a VPN [1-38]: " + bcolors.ENDC)

    if choice==1: #BASIC#

	os.system("openvpn ")
	import modules.option_1
	import modules.clear

    elif choice==2:

	import modules.clear
	import modules.option_2
        import modules.wifi.wireless_setup
    	print bcolors.WARNING + "\n[!]. Rebooting For Changes to Take Effect." + bcolors.ENDC
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        os.system("sudo reboot now")

    elif choice==3:

	import modules.clear
        import modules.option_3
        import modules.wifi.wireless_setup

    elif choice==4: #PRIVACY#

	import modules.clear
	import modules.privacy.option_4
        import modules.wifi.wireless_setup

    elif choice==5:

	import modules.clear
        import modules.privacy.option_5
        import modules.wifi.wireless_setup
    	print bcolors.WARNING + "\n[!]. Rebooting For Changes to Take Effect." + bcolors.ENDC
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        os.system("sudo reboot now")

    elif choice==6:

	import modules.clear
	import modules.privacy.option_6
	print bcolors.WARNING + "\n[!]. Rebooting For Changes to Take Effect." + bcolors.ENDC
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        os.system("sudo reboot now")

    elif choice==7:

	import modules.clear
	import modules.option_2
        import modules.wifi.wireless_setup

    elif choice==8:

	import modules.clear
        import modules.privacy.option_3
        import modules.wifi.wireless_setup
    	print bcolors.WARNING + "\n[!]. Rebooting For Changes to Take Effect." + bcolors.ENDC
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        os.system("sudo reboot now")

    elif choice==9:

	import modules.clear
	import modules.privacy.option_4
	print bcolors.WARNING + "\n[!]. Rebooting For Changes to Take Effect." + bcolors.ENDC
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        os.system("sudo reboot now")

    elif choice==10:

	import modules.clear
        import modules.privacy.option_5
        import modules.wifi.wireless_setup

    elif choice==11:

	import modules.clear
	import modules.privacy.option_6
        import modules.wifi.wireless_setup
    	print bcolors.WARNING + "\n[!]. Rebooting For Changes to Take Effect." + bcolors.ENDC
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        os.system("sudo reboot now")

    elif choice==12:

	import modules.clear
	import modules.wifi.wpa_supplicant
    	print bcolors.WARNING + "\n[!]. Rebooting For Changes to Take Effect." + bcolors.ENDC
        cont = raw_input("\n[!]...Press 'Return' to Continue: ")
        os.system("sudo reboot now")

    elif choice==13:

	import modules.clear
	import modules.option_8
	import modules.clear

    elif choice==14:

        import modules.clear
        import modules.wifi.wireless_setup
        import modules.clear

    elif choice==15:

        import modules.clear
        import modules.update
        import modules.clear

    elif choice==16:

        print bcolors.GREEN + "\nThanks for using RaspN3t" + bcolors.ENDC
        loop=False

    else:

        raw_input(bcolors.RED + "\n[!]-Error That was a invalid Number, \n\nSelect from [1-38]" + bcolors.ENDC)
