#EX: Exceptions

# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
    
        print(int(a/b))
    except (ValueError) as e:
        print(f"Error Code: {e}") 
    # since the solution uses an old error message I have to print it manually
    except (ZeroDivisionError):
        print("Error Code: integer division or modulo by zero")

#testing new lines of code on git