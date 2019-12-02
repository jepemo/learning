#!/usr/bin/env python3

import math

test1 = [1,0,0,0,99]
test2 = [2,3,0,3,99]
test3 = [2,4,4,5,99,0]
test4 = [1,1,1,4,99,5,6,0,99]

def read_input():
	with open("input.txt", "r") as f:
		content = f.read()
		values = content.split(",")
		return map(int, values)
		
def fix_machine_code(machine_code):
	machine_code[1] = 12
	machine_code[2] = 2
	return machine_code
	
def execute(machine_code):
	it = 0
	last_pos_code = len(machine_code)
	while it < last_pos_code:
		op = machine_code[it]
		if op == 1:
			pos1 = machine_code[it+1]
			pos2 = machine_code[it+2]
			pos3 = machine_code[it+3]
			
			val1 = machine_code[pos1]
			val2 = machine_code[pos2]
			machine_code[pos3] = val1 + val2
			it += 4
		elif op == 2:
			pos1 = machine_code[it+1]
			pos2 = machine_code[it+2]
			pos3 = machine_code[it+3]
			
			val1 = machine_code[pos1]
			val2 = machine_code[pos2]
			machine_code[pos3] = val1 * val2
			it += 4
		elif op == 99:
			return machine_code
	return machine_code
	
if __name__ == "__main__":
	machine_code = read_input()
	# machine_code = test4
	# print(machine_code)
	machine_code = fix_machine_code(machine_code)
	# print(machine_code)
	result = execute(machine_code)
	# print(result[0])
	print(result)
