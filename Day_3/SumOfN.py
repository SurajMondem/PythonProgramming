#Algorithm to Display the sum of n natural numbers

number = int(input("Enter the Value of N: "))
totalSum = 0

for x in range(0, number + 1):
    totalSum = totalSum + x

print(totalSum)