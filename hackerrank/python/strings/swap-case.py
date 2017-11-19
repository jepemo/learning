def swap_char(c):
    return c.upper() if not c.istitle() else c.lower()

def swap_case(s):
    return ''.join([swap_char(c) for c in s])
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
