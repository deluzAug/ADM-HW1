def is_leap(year):
    leap = False
    if not 1900<= year <= 10**5:
            raise Exception('Year out of constraints')
    if year % 4 == 0 and year % 100 !=0:
            return not leap
    elif year % 4 == 0 and year % 100 == 0: 
            if year % 400 == 0:
                    return not leap
            else: return leap
    else: return leap
    