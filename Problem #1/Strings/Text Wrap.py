import textwrap

def wrap(string, max_width):
    new_string = textwrap.fill(string, max_width)
    return(new_string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)