if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    result = sum(student_marks[query_name])/len(student_marks[query_name])
    #since rounding wouldn't work I need to use f-string formatting
    result = f"{result:.2f}"
    print(result)
