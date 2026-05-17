# Task 3: Lambda Function: Gst Calculator

# Create a lambda function gst that price after adding 18% GST

# Add GST to price
gst = lambda price:price + (0.18 * price)

# calculate final price after GST and discount
final_price = lambda price,discount:gst(price) - discount

# Example usage
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount amount: "))  
final_price_with_discount = final_price(price, discount)
final_price_with_gst = gst(price)
print(f"\nThe final price after adding GST is: {final_price_with_gst:.2f} ")
print(f"\nThe final price after applying discount and adding GST is: {final_price_with_discount:.2f} \n") 



