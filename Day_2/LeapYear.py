# Algorithm to Check whether a year is leap year or not

Year = int(input("Enter the Year: "))

isLeapYear = False

if ((Year % 4 == 0) and (Year % 100 != 0)) or Year % 400 == 0:
    isLeapYear = True

print(isLeapYear)
