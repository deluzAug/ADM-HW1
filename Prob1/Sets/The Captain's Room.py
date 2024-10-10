# Enter your code here. Read input from STDIN. Print output to STDOUT
K = input()
list_rooms = list(map(int, input().split()))
set_rooms = set(list_rooms)
for i in set_rooms:
    list_rooms.remove(i)
    if i not in list_rooms:
        print(i)
