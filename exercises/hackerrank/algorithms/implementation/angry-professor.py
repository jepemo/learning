numTests = int(input())

for it in range(0, numTests):
    n, k = map(int, input().split())
    times = map(int, input().split())
    
    inClass = 0
    for t in times:
        if t < 0 or t == 0:
            inClass = inClass + 1
            
    if inClass >= k:
        print("NO")
    else:
        print("YES")
