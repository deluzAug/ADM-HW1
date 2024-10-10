#I lost 1 hour working on this wondering how I could obtain the same result every time if pop() is supposed to remove a random element and also 
# handling the invitable KeyError raised to discover that my code was fine but I needed to use the Python 3 settings above instead of pypy3... 
# (this I discovered looking at the discussion in the forum)
len_set = int(input())
set_val = {int(x) for x in input().split()}
N = int(input())
Commands = [input().split() for i in range(N)]
for i in Commands:
    try:
        if len(i) == 2:
            exec(f"set_val.{i[0]}({i[1]})")
        else:
            exec(f"set_val.{i[0]}()")
    except KeyError:
        pass  # Ignore the KeyError and continue with the next command

print(sum(set_val))
