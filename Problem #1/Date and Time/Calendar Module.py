# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
month, day, year = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(year, month, day)].upper()) 
