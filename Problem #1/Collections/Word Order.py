# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
words = OrderedDict()
for i in range(int(input())):
    word = input()
    if word in words.keys():
        words[word] +=1
    else:
        words[word] = 1
print(len(words.keys()))        
print(*words.values())
    
