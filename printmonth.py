import string

def getDates(day, month, dates):
    i = 0
    weekdays = dict({'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6})
    if month.lower() == "february":
        dates.pop()
        dates.pop()

    while i < weekdays.get(day):
        dates.insert(0, 0)
        i+=1
    j = 0
    if(month.lower() != "february"):
        endPadding = 42 - len(dates)
    else:
        endPadding = 40 - len(dates)
    
    while j < endPadding:
        dates.append(0)
        j+=1

    return dates

def splitArray(dates, cols):
    array = []
    for i in range(0, len(dates), cols):
        array.append(dates[i:i+cols])
    return array

def printDates(dates):
    for i in range(len(dates)):
        for j in range(len(dates[i])):
            if j < len(dates[i]) - 1:
                if dates[i][j] == 0:
                    print("   ", end='')
                else:
                    if dates[i][j] < 10:
                        print('{:2d} '.format(dates[i][j]), end='')
                    else:
                        print('{:1d} '.format(dates[i][j]), end='')
            else:
                if dates[i][j] == 0:
                    print(" ", end='')
                else:
                    print('{:2d} '.format(dates[i][j]), end='\n')
    print()

month = (input("Enter the month ('January, ..., 'December'):\n"))
day = (input("Enter the month ('Monday, ..., 'Sunday'):\n"))
weekdays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

print(month)

i = 0

while(i < len(weekdays)) :
    if(i < len(weekdays)-1):
        print(weekdays[i] + " ", end='')
    else:
        print(weekdays[i], end='\n')
    i+=1


dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

cols = 7

paddedDates = getDates(day, month, dates)
splitDates = splitArray(dates, cols)
printDates(splitDates)
