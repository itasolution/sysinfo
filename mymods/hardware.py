#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ################################################
#
# Get system informations
# - CPU informations
# - RAM statistics
# 
# Written by: Eugenio Palumbo, www.itasolution.it
#
# ################################################

from ._utils import nice_title, human_readable
import psutil

def get_cpuinfo():
	nice_title("CPU Informations")
	print("Physical cores:", psutil.cpu_count(logical=False))
	print("Total cores:", psutil.cpu_count(logical=True))
	cpufreq = psutil.cpu_freq()
	print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
	print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
	print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

	print("CPU Usage Per Core:")
	cpu_perc= psutil.cpu_percent(percpu=True, interval=1)
	for i, percentage in enumerate(cpu_perc):
		print(f"Core {i}: {percentage}%")
	print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def get_meminfo():
	nice_title("Memory Information")
	svmem = psutil.virtual_memory()
	print(f"Total: {human_readable(svmem.total)}")
	print(f"Available: {human_readable(svmem.available)}")
	print(f"Used: {human_readable(svmem.used)}")
	print(f"Percentage: {svmem.percent}%")

	nice_title("SWAP")
	swap = psutil.swap_memory()
	print(f"Total: {human_readable(swap.total)}")
	print(f"Free: {human_readable(swap.free)}")
	print(f"Used: {human_readable(swap.used)}")
	print(f"Percentage: {swap.percent}%")
