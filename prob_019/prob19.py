'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
def isLeap(year):
    if(year%400):
        return True
    elif(year%4):
        return True
    return False

def sundays():
    total = 0
    year = 1900
    dayOfWeek = 1

    months = {
        1: 31,
        2: 38,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    while(year != 2001):
        for m in range(1,13):
            daysOfMonth = months[m]
            if isLeap(year) and m == 2:
                daysOfMonth = daysOfMonth + 1
            for d in range(1,months[m]+1):
                # print("Year: ", year, ", Month: ", m, ", Day: ", d)
                if(d == 1 and dayOfWeek == 7 and year > 1900):
                    total = total + 1
                dayOfWeek = (dayOfWeek % 7) + 1
        year = year + 1

    return total

def main():
    print(sundays())

if __name__ == '__main__':
    main()