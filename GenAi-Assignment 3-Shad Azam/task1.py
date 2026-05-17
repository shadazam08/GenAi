# Task 1: Basic Function: Price After Discount

def apply_discount(price, discount_percent=5):
    """
    This function takes a price and an optional discount percentage (default is 5%) and returns the final price after applying the discount. It also includes a check to ensure that the discount percentage is not unreasonably high (e.g., 60% or more), in which case it will print a warning and return None.
    """
    if discount_percent >= 60:
        print("Warning: Discount percentage is unusually high.")
        return None
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price

# Example usage
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage ") or 5)
final_price = apply_discount(original_price, discount_percentage)
# Check if final_price is not None before printing the result to handle cases where the discount percentage is too high.
if final_price is not None:
    print(f"The price after applying a {discount_percentage}% discount is: {final_price:.2f}")
