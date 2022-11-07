#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ################################################
#
# Get system informations
# - Utility functions
# 
# Written by: Eugenio Palumbo, www.itasolution.it
#
# ################################################


#
# Print title, same lenght
#
def nice_title(title):
	print()
	title_max_len= 100
	title_len= len(" " + title.strip() + " ")
	calc= (title_max_len - title_len) /2
	if (calc % 2) == 0:
		print("=" * int(calc), title.strip(), "=" * int(calc))
	else:
		print("=" * int(calc), title.strip(), "=" * (int(calc) +1))

#
# Unit of measure in human-readable format
#
def human_readable(bytes, suffix="B"):
    factor = 1024
    for prefix in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{prefix}{suffix}"
        bytes /= factor
