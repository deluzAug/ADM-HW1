def wrapper(f):
    def fun(l):
        formatted = []
        for number in l:
            # Remove prefixes tacking only the last 10 digits
            number = number[-10:]
            # we add the +91 at the beginning and introduce a space
            formatted.append(f"+91 {number[:5]} {number[5:]}")
        
        return f(formatted)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 



