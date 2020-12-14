import copy
import pprint
import sys
from functools import lru_cache

sys.setrecursionlimit(100000)

def file_lines(filename="input.txt"):
	with open(filename) as f:
		return f.read().split("\n")

def ints(str_list):
	return list(map(int, str_list))

def example():
	return """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split("\n")

def example2():
	return """16
10
15
5
1
11
7
19
6
12
4""".split("\n")

def example3():
	return """1
2
3""".split("\n")

def flatten(ll):
	res = []
	for l in ll:
		if type(l) == list:
			res.extend(flatten(l))
		else:
			res.append(l)
	
	return res
	
def print_tree(tree, ident=0):
	# symbol = "-" if ident % 2 == 0 else "#"
	symbol = "-"
	prefix = str(ident) + " " + symbol
	for i in range(0, ident):
		prefix += symbol
	
	for elem in tree:
		if type(elem) == list:
			print_tree(elem, ident=ident+1)
		else:
			print(prefix, elem)
		
	


CACHE = {}

def process(head, tail):
	next_heads = [x for x in tail if x >= head and x <= head + 3]
	if len(next_heads) == 0:
		return 1
	else:
		res = 0
		for next_head in next_heads:
			if next_head not in CACHE:
				next_tail = [x for x in tail if x != next_head and x != head]
				p_res = process(next_head, next_tail)
				
				CACHE[next_head] = p_res
				
				res += p_res
			else:
				res += CACHE[next_head]
				
		return res

def main():
	data = ints(file_lines())
	data.append(max(data) + 3)
	data = list(sorted(data))
	
	res = process(0, data)
	
	print("Res", res)

if __name__ == "__main__":
	main()
