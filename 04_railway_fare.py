# Assignment 4: Railway Fare and Reservation Calculator
# Calculate fare using distance slabs, age concession, and a reservation fee.

distance = int(input("Enter travel distance in km: "))
age = int(input("Enter passenger age: "))

if distance <= 0 or age < 0:
    print("Enter a positive distance and a valid age.")
else:
    if distance <= 100:
        fare = distance * 2
    elif distance <= 300:
        fare = distance * 3
    else:
        fare = distance * 4

    if age < 12:
        fare *= 0.5
    elif age >= 60:
        fare *= 0.7

    fare += 30
    print("Final Railway Fare:", fare)
