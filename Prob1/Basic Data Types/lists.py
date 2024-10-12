if __name__ == '__main__':
    N = int(input())
    commands = [[ x for x in input().split()]for i in range(N)]
    array = list()
    for i in commands:
            if i[0] == "print":
                    print(array)
            elif i[0] == "insert":
                    array.insert(int(i[1]), int(i[2]))
            elif i[0] == "append":
                    array.append(int(i[1]))
            elif i[0] == "remove":
                    array.remove(int(i[1]))
            elif i[0] == "sort":
                    array.sort()
            elif i[0] == "pop":
                    array.pop(-1)
            elif i[0] == "reverse":
                    array.reverse()
    