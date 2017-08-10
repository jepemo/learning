dim = int(input())

matrix = []
for d in range(0, dim):
    matrix.append(input().split())
 
sum0 = 0
for d in range(0, dim):
    sum0 = sum0 + int(matrix[d][d])
    
sum1 = 0
for d in range(0, dim):
    sum1 = sum1 + int(matrix[dim-1-d][d])
    
print(abs(sum0-sum1))
