# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
Market = OrderedDict()
for i in range(int(input())):
    item_name, price = input().rsplit(' ', 1)
    if item_name in Market.keys():
        Market[item_name] += int(price)
    else:
        Market[item_name] = int(price)
for item_name, net_price in Market.items():
    print(f"{item_name} {net_price}")
