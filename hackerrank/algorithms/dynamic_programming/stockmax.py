def calc_mov(spent, shares, movs):
    #print(spent, shares, movs)
    spends = []
    if movs == None or len(movs) == 0:
        spends = [spent]
    else:
        val = movs[0]
        rest_movs = movs[1:]

        spends.extend(calc_mov(spent-val, shares+1, rest_movs))
        spends.extend(calc_mov(spent, shares, rest_movs))
        for i in range(1, shares+1):
            spends.extend(calc_mov(spent+val*i, shares-1, rest_movs))

    return spends


def calculate_day(movs):
    return max(calc_mov(0, 0, movs))

def read_input():
    num_days = int(input().strip())
    mov_days = []
    for l in range(0, num_days):
        num_movs = int(input().strip())
        mov_days.append(list(map(int, input().split())))

    return mov_days

mov_days = read_input()
for movs in mov_days:
    print(calculate_day(movs))
