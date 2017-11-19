n = int(input())

for i in range(0, n):
    for s in range(0, n-i-1):
        print(' ', end='')
        
    for b in range(0, i+1):
        print('#', end='')
    
    print ('')
