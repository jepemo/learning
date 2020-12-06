def load_data():
    with open("input.txt") as f:
        return f.read().split("\n")

def load_test_data():
    return [
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'BBFFBBFRLL'
    ]

def get_row_id(steps):
    pmin = 0
    pmax = 127
    # print("0", pmin, pmax)
    for s in steps:
        if s == "B":
            pmin = pmin + (pmax - pmin) // 2
        else:
            pmax = pmin + (pmax - pmin) // 2
        # print(s, pmin, pmax)
    return pmax

def get_col_id(steps):
    pmin = 0
    pmax = 7
    for s in steps:
        if s == "R":
            pmin = pmin + (pmax - pmin) // 2
        else:
            pmax = pmin + (pmax - pmin) // 2
    return pmax

def get_seat_id(seat):
    row_id = get_row_id(seat[0:7])
    col_id = get_col_id(seat[7:10])
    # print(row_id, col_id)
    return (row_id * 8)  + col_id

def get_my_seat_id(seat_ids):
    oids = list(sorted(seat_ids))
    # print(oids)
    min_seat_id = get_seat_id("FFFFFFFLLL") 
    max_seat_id = get_seat_id("BBBBBBBRRR")
    for ident in range(min_seat_id, max_seat_id):
        if (ident-1) in oids and (ident+1) in oids and ident not in oids:
            return ident
    return -1

def main():
    # seats = load_test_data()
    seats = load_data()
    seat_ids = [get_seat_id(seat) for seat in seats]
    print("Result", get_my_seat_id(seat_ids))

if __name__ == "__main__":
    main()
