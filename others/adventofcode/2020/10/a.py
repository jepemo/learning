import copy

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

def process0(ini, ilist):
	print(ini)
	compat = list(filter(lambda x: x >= ini - 3, ilist))
	#print(compat)
	num_elems = len(ilist)
	path = []
	for c in compat:
		l = copy.copy(ilist)
		l.remove(c)
		path = process0(c, l)
		if len(path) == num_elems:
			break
		
	res = [ini]
	res.extend(path)
	return res

def process(ini, data):
	data.append(ini)
	path = process0(0, list(sorted(data)))
	path = list(sorted(path))
	
	print(path)
	
	num1 = 0
	num3 = 0
	for i in range(1, len(path)):
		p0 = path[i-1]
		p1 = path[i]
		if p1 == p0 + 1:
			num1 += 1
		elif p1 == p0 + 3:
			num3 += 1
			
	return (num1, num3)
		

def main():
	data = ints(file_lines())
	#data = ints(example())
	ini = max(data) + 3
	res = process(ini, data)
	print("Res", res, res[0] * res[1])

if __name__ == "__main__":
	main()
