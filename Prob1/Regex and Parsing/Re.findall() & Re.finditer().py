# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
# regex is a nightmare, had to work with the documentation on the side to create the correct pattern
# This looks for a consonant as the start of the string to match but doesn't capture it.
# other than "lookbehind" I used "lookahaed"
pattern = r"(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])"

s = input()

result = re.finditer(pattern, s, re.IGNORECASE)

for match in result:
    print(match.group())

# initially forgot to add this...

if not list(re.finditer(pattern, s, re.IGNORECASE)):
    print(-1)
# this checks if the re.finditer() returned an empty iterable, transforming it into a list
# which if empty is converted into the False boolean by the if, so I add the not