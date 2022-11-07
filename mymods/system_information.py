#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ################################################
#
# Get system informations
# - OS information
# - Boot time
# - Uptime
# 
# Written by: Eugenio Palumbo, www.itasolution.it
#
# ################################################

from ._utils import nice_title
import platform
import psutil
from datetime import datetime

def sysinfo():
	nice_title("System Information")
	uname = platform.uname()
	print(f"OS: {uname.system}")
	print(f"Hostname: {uname.node}")
	print(f"Release: {uname.release}")
	print(f"Version: {uname.version}")
	print(f"Machine: {uname.machine}")
	print(f"Processor: {uname.processor}")

def get_boot_time():
	nice_title("Boot Time")
	timestamp = psutil.boot_time()
	dt_object = datetime.fromtimestamp(timestamp)
	print(f"Boot at: {dt_object.year}/{dt_object.month}/{dt_object.day} {dt_object.hour}:{dt_object.minute}:{dt_object.second}")

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    print(uptime_seconds)