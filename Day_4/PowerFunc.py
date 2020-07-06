# Algorithm and flow chart to Compute xy without using pow().

number = int(input("ENTER THE NO.: "))
power = int(input("ENTER THE POWER: "))
result = number
index = 0
if power == 0:
    print("RESULT: 1")
elif power == 1:
    print("RESULT: ", result)
else:
    while index != (power-1):
        result = result * number
        index += 1
    print("RESULT: ", result)