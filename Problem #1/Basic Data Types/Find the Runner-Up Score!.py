if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()
    x = arr.index(max(arr)) 
    print(arr[x-1])
    
