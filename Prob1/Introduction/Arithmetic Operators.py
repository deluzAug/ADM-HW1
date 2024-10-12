if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)
    
    if 1 <= a <=10^10 or 1 <= b <=10^10 : 
            raise Exception('error, value out of bound')
