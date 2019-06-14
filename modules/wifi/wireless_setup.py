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
    print "-----------------------------------------------"
    print "Select One of the Following Wireless Encryption"
    print "###############################################"
    print bcolors.WARNING + "[1]. NONE (OPEN)"
    print "[2]. WEP"
    print "[3]. WPA"
    print "[4]. WPA2"
    print "[5]. View Sample for wpa_supplicant.conf"
    print "[6]. Return to Main Menu" + bcolors.ENDC
    print "################################################"
    print "------------------------------------------------"

loop=True

while loop:
    print_menu()
    choice = input(bcolors.WARNING + "\nSelect an Option [1-6]: " + bcolors.ENDC)

    if choice==1:

	    import cyphers.open

    elif choice==2:

	    import cyphers.wep

    elif choice==3:

        import cyphers.wpa

    elif choice==4:

	    import cyphers.wpa2

    elif choice==5:

        import wpa_supplicant
        cont = raw_input(bcolors.WARNING + "\n[!]...Press 'Return' to Continue") + bcolors.ENDC

    elif choice==6:

        loop=False

    else:

        raw_input(bcolors.RED + "\n[!]-Error That was a invalid Number, \n\nSelect from [1-6]" + bcolors.ENDC)
