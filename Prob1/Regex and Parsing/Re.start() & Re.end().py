# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
String = input()
pattern = input()
# of course this exercise wants you to find overlapping matches...
# so I cannot use finditer() or findall() as I initially thought
# the only way I thought of doing this is by sliding through the string...


# Initialize starting position for searching
window_start = 0
found = False
# Looping with while
while True:
    
    match = re.search(pattern, String[window_start:])
    # this closes the loop if no matches are found, no match => search returns None
    if not match:
        break
    # Calculate the start and end index in the original string
    # I need to take the window starting position in the original string and add the match.start() in the slices string
    start_index = window_start + match.start()
    # same reasoning for the end
    end_index = window_start + match.end() - 1
    print(f"({start_index}, {end_index})")
    found = True
    window_start = start_index + 1

if not found:
    print("(-1, -1)")
 