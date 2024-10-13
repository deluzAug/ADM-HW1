if __name__ == '__main__':
    n = int(input())
    
    if n < 1 or n > 20:
        raise Exception('Number out of constraints')
    
    for i in range(0,n):
        print(i**2)        
