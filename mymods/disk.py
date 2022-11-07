#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ################################################
#
# Get system informations
# - Partition informations, mount point, space info
# 
# Written by: Eugenio Palumbo, www.itasolution.it
#
# ################################################

from ._utils import nice_title, human_readable
import psutil

def get_disk_info():
	nice_title("Disk Information")
	print()
	print(f"Devices list:")
	print()

	partitions = psutil.disk_partitions()
	unreadable = 0
	for partition in partitions:
		print(f"=== Device: {partition.device} ===")
		print(f"  Mountpoint: {partition.mountpoint}")
		print(f"  File system type: {partition.fstype}")
		try:
			partition_usage = psutil.disk_usage(partition.mountpoint)
		except PermissionError:
			# this can be catched due to the disk that
			# isn't ready
			unreadable = unreadable + 1
			continue
		print(f"  Total Size: {human_readable(partition_usage.total)}")
		print(f"  Used: {human_readable(partition_usage.used)}")
		print(f"  Free: {human_readable(partition_usage.free)}")
		print(f"  Percentage: {partition_usage.percent}%")
	print()
	print(f"Partition unreadable due to disk not ready: {unreadable}")
