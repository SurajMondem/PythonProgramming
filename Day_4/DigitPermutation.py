# Algorithm to Rotate the given number for all permutations: Input: 3256


number = int(input("Enter the number: "))
switch = True
firstDigit = int(number) % 10
digit = firstDigit
length = len(str(number))
while (digit != firstDigit) or switch:
    switch = False
    number = int(number) / 10
    number = int(number) + digit * (10**(length-1))
    print(number)
    digit = int(number) % 10
