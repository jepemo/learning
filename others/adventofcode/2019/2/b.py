#!/usr/bin/env python3

import sys

def read_input():
	with open("input.txt", "r") as f:
		content = f.read()
		values = content.split(",")
		return map(int, values)
		
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
	
def fix_machine_code(i, j):
	machine_code[1] = i
	machine_code[2] = j
	return machine_code
	
if __name__ == "__main__":
	goal = 19690720
	
	for i in range(0, 100):
		for j in range(0, 100):
			machine_code = read_input()
			machine_code = fix_machine_code(i, j)
			result = execute(machine_code)
			pos_0 = result[0]
			
			if pos_0 == goal:
				noun = machine_code[1]
				verb = machine_code[2]
				print("noun={}, verb={}".format(noun, verb))
				print("res={}".format(100 * noun + verb))
				sys.exit(0)
				
	print "No result"
