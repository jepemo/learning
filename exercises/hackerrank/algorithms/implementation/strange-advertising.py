import math

level = int(input())

ini_people = 5
people_like = 0
total_like = 0
for i in range(1, level+1):
    people_like = math.floor(ini_people/2)
    total_like = total_like + people_like
    ini_people = (people_like * 3)
    

print(total_like)
