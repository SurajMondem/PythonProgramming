# Algorithm to Display the sum of individual digits in a number

number = int(input("Enter the number: "))
digitSum = 0

while number != 0:
    temp = int(number) % 10
    digitSum = digitSum + temp
    number /= 10

print(digitSum)
