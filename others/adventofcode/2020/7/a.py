import pprint

def load_data():
	with open("input.txt") as f:
		return f.read().split("\n")
		
def load_test_data():
	return """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split("\n")


def read_first_color(sp):
	sp2 = sp.split("bags")
	return sp2[0].strip()
	
def read_elems(combs):
	if combs.endswith("no other bags."):
		return {}
		
	sp = combs.split(",")
	elems = {}
	for e in sp:
		ms = e.split()
		color = ms[1] + " " + ms[2]
		num = int(ms[0])
		elems[color] = num
	
	return elems
		

def read_groups(data):
	groups = {}
	for line in data:
		sp = line.split("contain")
		color = read_first_color(sp[0])
		elems  = read_elems(sp[1]) if len(sp) > 1 else {}
		groups[color] = elems
		
	return groups
	
def process(groups, name, checked=[]):
	num = 0
	for gname, gelems in groups.items():
		if name in gelems.keys() and gname not in checked:
			checked.append(gname)
			num += process(groups, gname, checked) + 1
		
	return num

def main():
	data = load_data()
	groups = read_groups(data)
	# pprint.pprint(groups)
	res = process(groups, "shiny gold")
	print(res)
	

if __name__ == "__main__":
	main()
