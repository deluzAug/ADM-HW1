# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()

# Regex pattern to find the first repeating alphanumeric character
pattern = r'([a-zA-Z0-9])\1'
# I cannot use the expression \w because it matches also the underscore character
# this uses backreference, \1 captures the same characters contained in the first group, which in this case is (\w)

# Search for the pattern in the string, we cannot use match cause it only checks for a match only at the beginning of the string
match = re.search(pattern, s)

# Check if there is a match and print the captured group
if match:
    print(match.group(1))  # Output the first repeating character
else:
    print(-1)  # No repeating character found


