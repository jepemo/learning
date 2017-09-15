def count_substring(string, sub_string):
    num = 0
    for ind in range(len(string)):
        if len(string[ind:]) >= len(sub_string):
            if string[ind:ind+len(sub_string)] == sub_string:
                num += 1
    
    return num
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
