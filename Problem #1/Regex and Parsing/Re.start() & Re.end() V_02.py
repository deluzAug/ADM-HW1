#modified this after having reread the documentation for lookahead, now much faster and cleaner
import re
String = input()
pattern = rf"(?=({input()}))"

list = [(m.start(), m.end()+len(pattern[3:-4])) for m in re.finditer(pattern, String)]

# had to adjust the end with the length of the matched pattern

if list:
    for i in list:
        print(i)
else:
    print((-1, -1))
