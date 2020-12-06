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
    group_persons = {}
    groupid = 1
    num_persons = 0
    for line in data:
        if line.strip() == "":
            groupid += 1
            num_persons = 0
            continue
        else:
            num_persons += 1
            if groupid not in groups:
                groups[groupid] = {}
            ansg = groups[groupid]
            for c in line:
                if c not in ansg:
                    ansg[c] = 1
                else:
                    ansg[c] += 1
            groups[groupid] = ansg
            group_persons[groupid] = num_persons

    return groups, group_persons

def get_groups_result(groups, group_persons):
    res = 0
    for gk, gv in groups.items():
        num_persons = group_persons[gk]
        num_answers = 0
        for _ak, av in gv.items():
            if av == num_persons:
                num_answers += 1
        res += num_answers

    return res

def main():
    data = load_data()
    groups, group_persons = get_group_answers(data)
    res = get_groups_result(groups, group_persons)
    print("Result", res)

if __name__ == "__main__":
    main()
