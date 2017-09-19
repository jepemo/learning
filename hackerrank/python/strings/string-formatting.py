
def normal(num):
    return "{0}".format(num)
def octal(num):
    return "{0}".format(oct(num)).replace("0o", "")
def hexadecimal(num):
    return "{0}".format(hex(num)).replace("0x", "").upper()
def binario(num):
    return "{0}".format(bin(num)).replace("0b", "")

def print_formatted(number):
    numsList = []
    for i in range(1, number+1):
        numsList.append([normal(i), octal(i), hexadecimal(i), binario(i)])
        
    margin=len(numsList[len(numsList)-1][3])+1
    for line in numsList:
        n = line[0]
        o = line[1]
        h = line[2]
        b = line[3]
        print(n.rjust(margin-1)+o.rjust(margin)+h.rjust(margin)+b.rjust(margin))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
