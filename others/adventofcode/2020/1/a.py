import sys

def read_input():
	with open("input.txt", "r") as f:
		return f.read()
		
def get_list_numbers_input():
	data = read_input()
	result = []
	for line in data.split("\n"):
		result.append(int(line))
	return result
		
def main():
	numbers = get_list_numbers_input()
	num_numbers = len(numbers)
	print("Num numbers:", num_numbers)
	for i in range(0, num_numbers):
		for j in range(i+1, num_numbers):
			n0 = numbers[i]
			n1 = numbers[j]
			res_sum = n0 + n1
			if  res_sum == 2020:
				print("Numbers:", n0, n1, "Result:", n0 * n1)
				sys.exit(0)
				
	print("No Result?")
	
if __name__ == "__main__":
	main()
