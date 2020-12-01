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
			for k in range(i+2, num_numbers):
				n0 = numbers[i]
				n1 = numbers[j]
				n2 = numbers[k]
				res_sum = n0 + n1 + n2
				if  res_sum == 2020:
					print("Numbers:", n0, n1, n2, "Result:", n0 * n1 * n2)
					sys.exit(0)
				
	print("No Result?")
	
if __name__ == "__main__":
	main()
