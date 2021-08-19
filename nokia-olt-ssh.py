#!/usr/bin/env python3
#-----------------------------------------------------------------------
# Simple script to connecto with SSH to NOKIA / ALCATEL OLTs ISAN FX8, FX16
# Written by Jorge Luiz Taioque
#
# Dependences python3 and netmiko
# apt install python3
# apt install python3-pip
# apt install python3-netmiko
#-----------------------------------------------------------------------

__author__ = 'Jorge Luiz Taioque'
__version__= 1.0

# impor netmiko library
from netmiko import ConnectHandler

# To use other device type
# huawei
# juniper
# juniper_junos

# create paramiter of connections
nokia = {
	'device_type': 'alcatel_aos',
	'host': '10.10.10.1',
	'username': 'isadmin',
	'password': 'password',
	}

# Connect to OLT
net_connect = ConnectHandler(**nokia)

# show terminal to prove connection
net_connect.find_prompt()

#send command
output = net_connect.send_command("show equipment slot")

# get output
print (output)

# disconect ssh connection
net_connect.disconnect()
