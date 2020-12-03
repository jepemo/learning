TREE_SYMBOL = "#"

def traspose(m):
	return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 		

def load_input():
	with open("input.txt", "r") as f:
		lines = f.read().split("\n")
		m = []
		for line in lines:
			m.append([x for x in line])
		return m
		
def get_value(m, position):
	num_rows = len(m)
	num_cols = len(m[0])
	x, y = position
	if x < num_cols:
		return m[y][x]
	else:
		x_pos = x % len(m[0])
		return m[y][x_pos]
	
def get_next_position(position, inc_x, inc_y):
	x, y = position
	return (x+inc_x, y+inc_y)
	
def valid_position(m, position):
	num_rows = len(m)
	num_cols = len(m[0])
	x, y = position
	return y < num_rows #and x < num_cols
		
def walk(m, inc_x, inc_y):
	end = False
	position = (0, 0)
	num_trees = 0
	while not end:
		value = get_value(m, position)
		# print(position, value)
		if value == TREE_SYMBOL:
			num_trees += 1
		position = get_next_position(position, inc_x, inc_y)
		if not valid_position(m, position):
			end = True
			
	return num_trees

def main():
	m = load_input()
	# m = list(reversed(traspose(m)))
	res = 1
	for p in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
		x_inc, y_inc = p
		res *= walk(m, x_inc, y_inc)
	print("Res", res)

if __name__ == "__main__":
	main()
