def load_data():
	with open("input.txt") as f:
		return f.read().split("\n")
	
def load_test_data():
	return """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split("\n")

def valid(nums, num):
	# print(num, nums)
	for i in range(0, len(nums)):
		for j in range(i, len(nums)):
			n0 = nums[i]
			n1 = nums[j]
			if n0 != n1 and (n0 + n1) == num:
				return True
	return False

def check(nums, preamble):
	for ind in range(preamble, len(nums)-preamble):
		num = nums[ind]
		lastn_nums = nums[ind-preamble:ind] 
		if not valid(lastn_nums, num):
			return num
			
def get_min_max(nums):
	return min(nums), max(nums)
			
def get_res(nums, inv_num):
	for i in range(0, len(nums)):
		acc = 0
		for j in range(i, len(nums)):
			r = nums[i:j]
			acc = sum(r)
			if acc == inv_num:
				minv, maxv = get_min_max(r)
				return minv + maxv
			elif acc > inv_num:
				break
				
	return -1
			
	
	
def main():
	lines = load_data()
	nums = list(map(int, lines))
	invalid_number = check(nums, 25)
	res = get_res(nums, invalid_number)
	print("Res", res)
	
		
if __name__ == "__main__":
	main()
