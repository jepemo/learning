if __name__ == '__main__':
    N = int(input())
    L = []
    for n in range(0, N):
        cmd_args = input().split()
        cmd = cmd_args[0]
        if cmd == "print":
            print(L)
        elif cmd == "sort":
            L.sort()#sorted(L)
        elif cmd == "reverse":
            L.reverse()
        elif cmd == "insert":
            L.insert(int(cmd_args[1]), int(cmd_args[2]))
        elif cmd == "pop":
            L.pop()
        elif cmd == "append":
            L.append(int(cmd_args[1]))
        elif cmd == "remove":
            L.remove(int(cmd_args[1]))
