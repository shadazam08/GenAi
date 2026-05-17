# Task 5: using filter(): filter expensive Products

# Given a list of product prices
prices = [100, 250, 400, 1200, 50, 2000, 850]

# check if the price is greater than 500
is_expensive = lambda price: price > 500
# check if the price is less than or equal to 500
is_cheap = lambda price: price <= 500

# Use the filter() function to filter out expensive products from the list and also filter out cheap products from the list
expensive_products = list(filter(is_expensive, prices))
cheap_products = list(filter(is_cheap, prices))

# Print the expensive products
print(f"\nExpensive Products: {expensive_products}\n")
# Print the cheap products
print(f"Cheap Products: {cheap_products}\n")
