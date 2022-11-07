#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ################################################
#
# Get system informations
# - Get IP Address, Netmask, MAC Address
# - Get traffic informations
# 
# Written by: Eugenio Palumbo, www.itasolution.it
#
# ################################################

from ._utils import nice_title, human_readable
import psutil

def get_net_ip():
	nice_title("Network Information")
	if_addrs = psutil.net_if_addrs()
	#print(if_addrs)
	for interface in if_addrs.items():
		print(f"=== {interface[0]} ===")
		for address in interface[1]:
			#print(address)
			if str(address.family) == 'AddressFamily.AF_INET':
				print(f"  IPv4 Address: {address.address}")
				print(f"  Netmask: {address.netmask}")
				print(f"  Broadcast IP: {address.broadcast}")
				print()
			elif str(address.family) == 'AddressFamily.AF_INET6':
				print(f"  IPv6 Address: {address.address}")
				print(f"  Netmask: {address.netmask}")
				print(f"  Broadcast IP: {address.broadcast}")
				print()
			elif str(address.family) == 'AddressFamily.AF_PACKET':
				print(f"  MAC Address: {address.address}")
				print(f"  Netmask: {address.netmask}")
				print(f"  Broadcast MAC: {address.broadcast}")
				print()

def get_net_traffic():
	nice_title("Network Information (since boot)")
	net_io = psutil.net_io_counters()
	print(f"Total Bytes Sent: {human_readable(net_io.bytes_sent)}")
	print(f"Total Bytes Received: {human_readable(net_io.bytes_recv)}")

