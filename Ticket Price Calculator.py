age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").strip().capitalize()

if age < 12:
    price = 20
elif age <= 17:
    price = 35
elif age <= 59:
    price = 50
else:
    price = 25

if day == "Tuesday":
    price = price - 10
    if price < 10:
        price = 10

print("Final ticket price:", price, "SAR")
