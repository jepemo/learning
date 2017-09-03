if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    uniq = set(arr)
    L = list(uniq)
    #print(L)
    L = sorted(L, key=lambda x: x)
    #print(L)
    L.reverse()
    #print(L)
    print(L[1])
