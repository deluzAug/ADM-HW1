if __name__ == '__main__':
    s = input()
    commands = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    for command in commands :
        print(any(eval("letter." + command + "()") for letter in s))
    
