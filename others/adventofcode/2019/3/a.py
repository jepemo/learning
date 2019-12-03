#!/usr/bin/env python3

# MAX_DIM_BOARD = 30000

# [Input, Output]
TESTS = [
["""R8,U5,L5,D3
U7,R6,D4,L4""",6],
["""R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83""", 159],
["""R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7""", 135]
]

class Matrix:
	def __init__(self):
		self.nodes = {}
		
	def set(self, x, y, value):
		key = "{}#{}".format(x,y)
		self.nodes[key] = value
		# print(self.nodes)
		
	def get(self, x, y):
		key = "{}#{}".format(x,y)
		if key in self.nodes:
			return self.nodes[key]
		else:
			return None
			
	def values(self):
		for key, value in self.nodes.items():
			coord = key.split("#")
			# print(coord, key)
			yield (int(coord[0]), int(coord[1]), value)
			
	def pprint(self):
		print("m:")
		print(self.nodes)
			

def parse_input_lines(lines):
	wires = []
	for line in lines:
		wires.append(line.strip().split(","))
	return wires


def read_input():
	with open("input.txt", "r") as f:
		lines = f.readlines()
		return parse_input_lines(lines)
		
		
def initialize_wires_boards(number_of_wires):
	wires_boards = []
	for i in range(number_of_wires):
		# matrix = [[0 for x in range(MAX_DIM_BOARD)] 
		          # for i in range(MAX_DIM_BOARD)]
		# wires_boards.append(matrix)
		wires_boards.append(Matrix())
	return wires_boards
	
	
def print_boards(wires_boards):
	for wb in wires_boards:
		wb.pprint()
		# print ("Wire:")
		# for r in wb:
			# for c in r:
				# print(c, end=',')
			# print("")
		
			
def connect_wires_to_board(wires_paths, wires_boards, ini_pos):
	output_boards = []
	for it in range(len(wires_paths)):
		matrix = wires_boards[it]
		wire_path = wires_paths[it]
		
		x_pos = ini_pos
		y_pos = ini_pos
		
		# matrix[y_pos][x_pos] = 1
		
		for step in wire_path:
			dir = step[0]
			dis = int(step[1:])
			for s in range(dis):
				if dir == 'U':
					y_pos += 1
				elif dir == 'R':
					x_pos += 1
				elif dir == 'D':
					y_pos -= 1
				elif dir == 'L':
					x_pos -= 1
				
				# print(x_pos, y_pos)
				# matrix[y_pos][x_pos] = 1
				matrix.set(x_pos, y_pos, 1)
				# print(matrix.nodes)
			
		output_boards.append(matrix)
	return output_boards
	
def calculate_hamming_distance(x1, y1, x2, y2):
	return abs(x1-x2) + abs(y1-y2)
	
def calculate_result(output_boards, ini_pos):
	result = 9999999999
	
	x_ini = ini_pos
	y_ini = ini_pos
	
	b1 = output_boards[0]
	b2 = output_boards[1]
	
	for (x, y, value) in b1.values():
		if b2.get(x, y) != None:
			distance = calculate_hamming_distance(x_ini, y_ini, x, y)
			if distance < result:
				result = distance
		
	# for x in range(MAX_DIM_BOARD):
		# for y in range(MAX_DIM_BOARD):
			# r1 = b1[y][x]
			# r2 = b2[y][x]
			# if r1 == 1 and r2 == 1:
				# distance = calculate_hamming_distance(x_ini, y_ini, x, y)
				# if distance < result:
					# # print(x_ini, y_ini, "-", x, y)
					# result = distance
	return result
		
		
if __name__ == "__main__":
	wires_paths = read_input()		
	# wires_paths = parse_input_lines(TESTS[2][0].split("\n"))
	# print(wires_paths)
	wires_boards = initialize_wires_boards(len(wires_paths))
	# print_boards(wires_boards)
	# ini_pos = int(MAX_DIM_BOARD / 2) - 1
	ini_pos = 0
	output_boards = connect_wires_to_board(wires_paths, wires_boards, ini_pos)
	# print_boards(wires_boards)
	result = calculate_result(output_boards, ini_pos)
	print(result)
	
