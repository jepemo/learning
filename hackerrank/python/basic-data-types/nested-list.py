if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])
      
    students = sorted(students, key=lambda x:x[1])
    lowest = students[0][1]
    second_lowest = None
    L = []
    for student in students:
        if student[1] == lowest:
            continue
        elif second_lowest == None:
            second_lowest = student[1]
            L.append(student[0])
        elif student[1] == second_lowest:
            L.append(student[0])
        else:
            continue
            
    L = sorted(L)
    for l in L:
        print(l)
            
    #print(students)
