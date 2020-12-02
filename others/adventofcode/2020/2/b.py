import sys

class PasswordEntry:
	def __init__(self, password, min_ocurrence, max_ocurrence, letter):
		self.password = password
		self.min_ocurrence = min_ocurrence
		self.max_ocurrence = max_ocurrence
		self.letter = letter
		
	@staticmethod
	def create_from_entry(entry):
		sp = entry.split()
		password = sp[2]
		letter = sp[1][:-1]
		sp2 = sp[0].split('-')
		min_ocurrence = int(sp2[0])
		max_ocurrence = int(sp2[1])
		return PasswordEntry(password, min_ocurrence, max_ocurrence, letter)
		
	def is_valid(self):
		num_ocurrences = 0
		p0 = self.password[self.min_ocurrence-1]
		p1 = self.password[self.max_ocurrence-1]
		
		if p0 == self.letter and p1 == self.letter:
			return False
		elif p0 == self.letter or p1 == self.letter:
			return True
		else:
			return False
	

def read_input():
	with open("input.txt", "r") as f:
		return f.read()
		
# def get_list_numbers_input():
	# data = read_input()
	# result = []
	# for line in data.split("\n"):
		# result.append(int(line))
	# return result
		
def main():
	raw_input = read_input()
	num_valids = 0
	for line in raw_input.split("\n"):
		pe = PasswordEntry.create_from_entry(line)
		if pe.is_valid():
			num_valids += 1
	
	print("Num. validos?", num_valids)
	
if __name__ == "__main__":
	main()
