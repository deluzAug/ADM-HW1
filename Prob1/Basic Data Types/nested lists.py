if __name__ == '__main__':
    students = list()
    scores = list()
    names = list()
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        students.append([name,score])
        if score not in scores:
                scores.append(score)
    scores.sort()
    second_low = scores[1]
    names = sorted([students[i][0] for i in range(0,len(students)) if students[i][1] == second_low], key = str.lower)
    #added the key = str.lower in case some names were provided with a lower case first letter as a mistake
    for i in names:
            print(i)