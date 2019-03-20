'''
Description: the function returns the exact day and month, using the year and
the number of days provided as arguments
Input: year - integer representing the year
       days - integer representing the number of days from the year
Output: month - the number of the month
        day - the day of the month
'''

def calculate_date(year, days):
    month = 0
    day = 0
    months = [31, 28 + (1 if year % 4 == 0 else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(1, 12):
        days = days - months[i - 1]
        if days <= 0:
            day = months[i - 1] + days
            month = i
            break
    return month, day


'''
Description: a function to print the results of the algorithm
'''

def print_date(year, month, day):
    print("The calendar date is: {}.{}.{}".format(day, month, year))


'''
Description: Main function that calls all the other functions
'''

def assignment7(year, days):
    if (days > 365 + 1 if year % 4 == 0 else 0):
        print("Invalid number of days")
    month, day = calculate_date(year, days)
    print_date(year, month, day)


'''
Unit testing function
'''

def testAssignment7():
    assert calculate_date(2018, 282) == (10, 9)
    assert calculate_date(2018, 1) == (1, 1)
    assert calculate_date(2012, 99) == (4, 8)
    assert calculate_date(2000, 240) == (8, 27)

testAssignment7()
year = int(input("Enter the year: "))
days = int(input("Enter the number of days: "))
assignment7(year, days)
