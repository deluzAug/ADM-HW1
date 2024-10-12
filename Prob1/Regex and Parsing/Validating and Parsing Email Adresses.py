
import re

N = int(input())
Contacts = [input().strip() for _ in range(N)]

# Regex pattern to validate the email
pattern = r"^[a-z][a-z0-9._-]*@[a-z]+\.[a-z]{1,3}$"

for contact in Contacts:
    name, email = contact.split()
    # Remove angle brackets around the email using slicing
    email = email[1:-1]
    
    if re.match(pattern, email, re.I):
        print(contact)

# I don't know if I should use Email.utils() to consider this exercise complete
# But it was much easier this way