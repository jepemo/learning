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
				if self._valid_field(key):
					num += 1
				
		num_keys = len(self._KEYS)
		if num == num_keys:
			return True
		elif num == num_keys - 1:
			if 'cid' not in self.values:
				return True
		else:
			return False
			
	def _valid_field(self, key):
		value = self.values[key]
		if key == "byr":
			if len(value) != 4:
				return False
			else:
				ival = int(value)
				return ival >= 1920 and ival <= 2002
		elif key == "iyr":
			if len(value) != 4:
				return False
			else:
				ival = int(value)
				return ival >= 2010 and ival <= 2020
		elif key == "eyr":
			if len(value) != 4:
				return False
			else:
				ival = int(value)
				return ival >= 2020 and ival <= 2030
		elif key == "hgt":
			if value.endswith("cm"):
				v = value.split("cm")
				ival = int(v[0])
				return ival >= 150 and ival <= 193
			elif value.endswith("in"):
				v = value.split("in")
				ival = int(v[0])
				return ival >= 59 and ival <= 76
			else:
				return False
		elif key == "hcl":
			if value.startswith("#"):
				res = value.split("#")
				code = res[1]
				if len(code) != 6:
					return False
				else:
					return sum([x.isdigit() or x.lower() in ['a', 'b', 'c', 'd', 'e', 'f'] for x in code]) == len(code)
			else:
				return False
		elif key == "ecl":
			return value.lower() in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
		elif key == "pid":
			return sum([x.isdigit() for x in value]) == len(value) and len(value) == 9
		elif key == "cid":
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
				# print(pp.values['pid'])
			pp = PassportInfo()
		else:
			pp.parse_line(line)
			
	if pp.is_valid():
		num_valids += 1
				
	print("Res", num_valids)

if __name__ == "__main__":
	main()
