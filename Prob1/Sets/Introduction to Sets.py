def average(array):
    array = set(array)
    n = len(array)
    avg = f"{sum(array)/n:.3f}"
    return(avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)