def read_input_lines():
	with open("input.txt") as f:
		return f.read().split("\n")

class PassportInfo:
	_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
	def __init__(self):
		self.values = {}
		
	def parse_line(self, line):
		sep = line.split(" ")
		for pair in sep:
			key, value = pair.split(":")
			self.values[key] = value
			
	def is_valid(self):
		num = 0
		for key in self._KEYS:
			if key in self.values:
				num += 1
				
		num_keys = len(self._KEYS)
		if num == num_keys:
			return True
		elif num == num_keys - 1:
			if 'cid' not in self.values:
				return True
		else:
			return False
			

def main():
	input_lines = read_input_lines()
	num_valids = 0
	pp = PassportInfo()
	for line in input_lines:
		if line == "":
			if pp.is_valid():
				num_valids += 1
			pp = PassportInfo()
		else:
			pp.parse_line(line)
			
	if pp.is_valid():
		num_valids += 1
				
	print("Res", num_valids)

if __name__ == "__main__":
	main()
