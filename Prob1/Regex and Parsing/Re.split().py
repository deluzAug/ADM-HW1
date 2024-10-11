regex_pattern = r"[.,]"	#set of characters that can be matched
import re
print("\n".join(re.split(regex_pattern, input())))