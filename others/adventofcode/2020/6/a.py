def load_data():
    with open("input.txt", "r") as f:
        return f.read().split("\n")

def load_test_data():
    return """abc

a
b
c

ab
ac

a
a
a
a

b
""".split("\n")

def get_group_answers(data):
    groups = {}
    groupid = 1
    for line in data:
        if line.strip() == "":
            groupid += 1
            continue
        else:
            if groupid not in groups:
                groups[groupid] = {}
            ansg = groups[groupid]
            for c in line:
                if c not in ansg:
                    ansg[c] = 1
            groups[groupid] = ansg

    return groups

def get_groups_result(groups):
    res = 0
    for g in groups.values():
        for v in g.values():
            res += v

    return res

def main():
    data = load_data()
    groups = get_group_answers(data)
    res = get_groups_result(groups)
    print("Result", res)

if __name__ == "__main__":
    main()
