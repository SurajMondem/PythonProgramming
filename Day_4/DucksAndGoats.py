# There are some goats and ducks in a farm. There are 60 eyes and 86 foot in total.
# Write a Python program to find number of goats and ducks in the farm

# You can use Cramer’s rule to solve the following 2 × 2 system of linear equation:
# ax + by = e
# cx + dy = f
#
# x = (ed – bf) / (ad – bc).
# y = (af – ec) / (ad – bc).

numOfEye = 62
numOfFoot = 90

goatLegs = 4
goatEyes = 2

duckLegs = 2
duckEyes = 2

numOfGoats = ((numOfEye * duckLegs) - (duckEyes * numOfFoot)) / ((goatEyes * duckLegs) - (duckEyes * goatLegs))
numOfDucks = ((goatEyes * numOfFoot) - (numOfEye * goatLegs)) / ((goatEyes * duckLegs) - (duckEyes * goatLegs))

print("THE NUMBER OF GOATS: ", numOfGoats)
print("THE NUMBER OF DUCKS: ", numOfDucks)
