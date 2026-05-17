# Task 4: using map(): Apply GST to a list prices

#given list of prices
prices = [100, 250, 400, 1200, 50]

# Create a lambda function to calculate price after adding 18% GST
gst = lambda price: price + (0.18 * price)
# Use the map() function to apply the gst lambda function to each price in the list
prices_with_gst = list(map(gst, prices))

# Print the original prices and the prices after adding GST
print(f"\nOriginal Prices: {prices} \n")
print(f"Prices after adding GST: {prices_with_gst}\n")

