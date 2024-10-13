# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
#let's create an empty list that will become our zip object
students_marks = list()

for _ in range(X):
    topic_marks = list(map(float, input().split()))
    #we append the list of votes for topic i
    students_marks.append(topic_marks)
    
#we calculate the average for each tuple created by zip, corresponding to the votes of each student
avg = [sum(i)/X for i in zip(*students_marks)]

#and then print with one decimal
for i in range(N):
    print(f"{avg[i]:.1f}")