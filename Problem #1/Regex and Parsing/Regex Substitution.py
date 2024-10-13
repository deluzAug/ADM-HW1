# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
lines = []

def check(match):
    if match.group(0) == '&&':
        return('and')
    elif match.group(0) == '||':
        return('or')

# same usage of lookahead and lookbehind notation, \s indicates a whitespace         
lines = [re.sub(r"(?<=\s)(&&|\|\|)(?=\s)", check, input()) for i in range(N)]
print("\n".join(lines))
