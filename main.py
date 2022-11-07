#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ################################################
#
# Get system informations
# 
# Written by: Eugenio Palumbo, www.itasolution.it
#
# ################################################

from mymods import system_information
from mymods import hardware
from mymods import network
from mymods import disk

if __name__ == "__main__":
	system_information.sysinfo()
	system_information.get_boot_time()
	system_information.get_uptime()
	hardware.get_cpuinfo()
	hardware.get_meminfo()
	network.get_net_ip()
	network.get_net_traffic()
	disk.get_disk_info()

	#input("Press ENTER to exit")