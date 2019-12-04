#!/usr/bin/env python3

import sys

MIN_VALUE = 402328
MAX_VALUE = 864247

def length_6(passw):
	str_pass = "{}".format(passw)
	return len(str_pass) == 6
	
def two_digits_same(passw):
	str_pass = "{}".format(passw)
	last_num = None
	for i in range(len(str_pass)):
		if i > 0:
			actual_num = int(str_pass[i])
			if actual_num == last_num:
				return True
		last_num = int(str_pass[i])
		
	return False
	
def digits_no_decrease(passw):
	str_pass = "{}".format(passw)
	last_num = None
	for i in range(len(str_pass)):
		if i > 0:
			actual_num = int(str_pass[i])
			if actual_num < last_num:
				return False
		last_num = int(str_pass[i])
		
	return True
	
def adjent_no_part_larger_group(passw):
	groups = {}
	str_pass = "{}".format(passw)
	last_num = None
	for i in range(len(str_pass)):
		key = "{}".format(str_pass[i])
		if key not in groups:
			groups[key] = 0
		
		if i > 0:
			actual_num = int(str_pass[i])
			if actual_num == last_num:
				if groups[key] == 0:
					groups[key] = 2
				else:
					groups[key] += 1
					
		last_num = int(str_pass[i])
		
	for key, value in groups.items():
		if value == 2:
			# print(passw)
			# print(groups)
			# sys.exit(0)
			return True
		
	return False

def check(passw):
	return length_6(passw) \
	   and two_digits_same(passw) \
	   and digits_no_decrease(passw) \
	   and adjent_no_part_larger_group(passw)

if __name__ == "__main__":
	passwords = []
	for i in range(MIN_VALUE, MAX_VALUE):
		if check(i):
			passwords.append(i)
			
	print(len(passwords))
