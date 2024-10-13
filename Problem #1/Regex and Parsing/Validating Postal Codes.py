regex_integer_in_range = r"([1-9])[0-9]{5}$"	
regex_alternating_repetitive_digit_pair = r"(?=(\d)(\d)\1)"	
# to solve this I had to read very carefully the documentation about lookaheads 
# I then discovered that the best way to force findall() to look also at overlapping
# patterns is to use lookahead... The way I did it in a previous ex. sliding with a while loop 
# was too complicated...

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)