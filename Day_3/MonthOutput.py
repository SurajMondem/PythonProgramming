# Algorithm to Display name of the month when month number is given.
# Algorithm to display name of the day when day number is given.

monthDictionary = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

weekDictionary = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday",
}

choice = int(input("Enter 1 for Month and 2 for week: "))

if choice == 1:
    number = int(input("Enter the number for Month: "))
    print(monthDictionary.get(number))
elif choice == 2:
    number = int(input("Enter the number for Week: "))
    print(weekDictionary.get(number))
