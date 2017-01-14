JAN = 0
FEB = 1
MAR = 2
APR = 3
MAY = 4
JUN = 5
JUL = 6
AUG = 7
SEP = 8
OCT = 9
NOV = 10
DEZ = 11

def monthDays(month, year):
    if month in [SEP, APR, JUN, NOV]:
        return 30
    if month in [JAN,MAR,MAY,JUL,AUG,OCT,NOV,DEZ]:
        return 31
    if month == FEB:
        if year%4==0 and (year%100 != 0 or year%400 == 0):
            return 29
        else:
            return 28

def sundays():
    days = 0 
    year = 1900
    month = 0
    sundays = 0
    yd = 0
    while year<2001:
        if year>=1901:
            if days%7 == 6: # sunday:
                sundays += 1

        days += monthDays(month,year)
        yd += monthDays(month,year)
        month += 1
        if month == 12:
            month = 0
            year += 1
            print("days %d/%d"%(year,yd))
            yd = 0
    return sundays








print(sundays())
