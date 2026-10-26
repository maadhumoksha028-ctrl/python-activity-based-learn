# Assignment 3: Hospital Billing and Patient Classification
# Apply a 10% concession when the total bill is at least 10,000.

consultation = float(input("Enter consultation charges: "))
tests = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

if consultation < 0 or tests < 0 or treatment < 0:
    print("Charges cannot be negative.")
else:
    total = consultation + tests + treatment

    if total >= 10000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount
    print("Total Bill:", total)
    print("Discount:", discount)
    print("Final Bill:", final_bill)
