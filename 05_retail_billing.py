# Assignment 5: Retail Billing with Discount
# Calculate the total price and apply a threshold-based discount.

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

if price < 0 or quantity < 0:
    print("Price and quantity cannot be negative.")
else:
    total = price * quantity

    if total >= 5000:
        discount = total * 0.15
    elif total >= 2000:
        discount = total * 0.10
    else:
        discount = 0

    final_amount = total - discount
    print("Total Amount:", total)
    print("Discount:", discount)
    print("Final Amount:", final_amount)
