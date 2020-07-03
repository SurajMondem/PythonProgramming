# Algorithm to Check whether a number is exactly divisible by 3 and 5 but not 6

Number = int(input("Enter the number: "))

if (Number % 3 == 0 and Number % 5 == 0) and Number % 6 != 0:
    print(Number, "is divisible by 3 and 5 but not 6")
else:
    print(Number, "is NOT divisible by 3 and 5 but not 6")