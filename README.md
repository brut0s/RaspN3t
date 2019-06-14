# What's RaspN3t?

RaspN3t is a easy to use Python Script, that transforms the Raspberry Pi into a Network Adapter.

  1. Ethernet to Wifi adapter.
  
  2. Ethernet to Wifi adapter with "TOR".
  
  3. Wireless to Ethernet adapter...COMMING SOON.
  
  4. Wireless to Ethernet adapter with "TOR"...COMMING SOON.
  
  5. Wifi Repeater...COMMING SOON.
  
  6. Wifi Repeater with "TOR"...COMMING SOON.
  
  7. Easy Wireless Connection Setup though Terminal.
  
  8. Change HotSpot Password.
  
  9. Added USB-Tethering Support.
  


![raspn3t](https://user-images.githubusercontent.com/25351355/42127537-883f00dc-7c68-11e8-9291-1ca9af678382.png)



RaspN3t also has the ability to setup a Wifi Connection, with addition security!!!!
With every wireless connection configuration from the main menu, RaspN3t does'nt keep a list of Saved Wifi Networks.
RaspN3t removes the setup and prevents the device from probing wich aids in secuiry due to Evil Twin Attacks.

For exampe if you Chose option 2,4,5,6 RaspN3t Deletes the wpa_supplicant file under "/etc/wpa_supplicant/wpa_supplicant.conf"
and replaces it with a new Config based on the Wireless Network you used to Connect to"

In future versions of RaspN3t, there will be other aditional security and privacy tools, such as:

 1. Support for OpenVPN.
 2. Macchanger at boot.
 3. Harden DNS.
 4. Display the Current Configuration based on IP-Tables [Ethernet----->-----Wifi-HotSpot] upon running RaspN3t.
  
 
Before You Run The Program Make sure you have 2 Wireless Cards pluged in, The Program is best used with 2 external Cards.
 
Having a hard time Connect to a wireless Network using Raspbian Lite?
Use my Official Script to Connect Raspbian Lite to a wifi Network with "EASE!!!"
"https://github.com/brut0s/Rasp-Connect"
 
 
 
 
 To Run:
 
 "git clone https://github.com/brut0s/RaspN3t"
 
 "cd RaspN3t"
 
 "sudo python install.py"
 
 The Installer will install and configure the HotSpot

 Run "sudo python raspn3t.py"
 to change adapter configuration, setup wifi, or change hotspot password.
 
 
 
 To Run Without Internet Access:
 
 Download the Zip and extract to a usb drive and copy the Files to a Destination on Raspbian
 
 then run:
 
 "cd RaspN3t"
 
 "sudo python raspn3t.py"
 
and select Option '9' and then the Pi Will Reboot, after reboot Run the "install.py" Script to Install and Configure the Raspberry Pi.
 
 
I Highly Recomend to use this Program with 2 Panda Wireless 300mbs adapters.

![images](https://user-images.githubusercontent.com/25351355/42129431-2bdbec9a-7c92-11e8-80d9-b8ab35340127.jpeg)

One for the Hotspot which is used by Default in this Program that gives you much better Signal compared to the internal one
and the Other is used to Connect to a Wireless Network, 
The Panda Offers Pretty Good Range for a HotSpot and also to connect to a Wireless Network. 
 
 

How To Update:

Update using "sudo python raspn3t.py" and select the update option.

Tested On Raspbian (Raspbian-Lite and Raspbian-Stretch)

For any problems please leave a comment.


