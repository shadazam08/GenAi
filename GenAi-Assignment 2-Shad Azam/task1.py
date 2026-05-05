# Task 1: Discount Rules (if / elif / else)


try:
    # 1. user input
    order_amount = int(input("Enter the order amount: "))

    # 2. discount rules
    if order_amount >= 2000:
        discount_rate = 0.15
    elif 1500 <= order_amount < 2000:
        discount_rate = 0.10
    elif 1000 <= order_amount < 1500:
        discount_rate = 0.07
    else:
        discount_rate = 0.0

    # 3. calculate final price
    discount = order_amount * discount_rate
    subtotal = order_amount - discount
    # Extra: calculate tax  5%
    tax_rate = 0.05
    tax = subtotal * tax_rate
    final_total = subtotal + tax

    # 4. output results
    print(f"Original order amount: {order_amount}")
    print(f"Discount applied: {discount:.2f} ({discount_rate*100:.0f}%)")
    print(f"Final price after discount: {subtotal:.2f}")
    print(f"Tax (5%): {tax:.2f}")
    print(f"Total amount to pay: {final_total:.2f}")

except ValueError:
    print("Invalid input. Please enter a numeric value for the order amount.")
