# Task 6: combined utility Function

def process_price(price):
    #use a map() + lambda to apply 10% discount to all price
    # Create a lambda function to calculate price after applying 10% discount
    discounted_prices = list(map(lambda p: p - (0.10 * p), price))
    #use filter() to keep only the discounted prices that are above 300
    # check if the price is greater than 300
    is_expensive = lambda price: price > 300

    filtered_price= list(filter(is_expensive, discounted_prices)) 

    return discounted_prices, filtered_price

# Example usage
prices = [100, 500, 900, 50, 750]
discounted_prices, filtered_price = process_price(prices)
print(f"\nDiscounted Prices: {discounted_prices}\n")
print(f"Filter discounted prices: {filtered_price}\n")

