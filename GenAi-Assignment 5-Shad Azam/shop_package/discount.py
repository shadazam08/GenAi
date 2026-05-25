# Task 3: discount.py

# create a function apply discount
def apply_discount(price, percent):
    discounted_amount = price-((percent / 100) * price)
    return discounted_amount

# create a function flat discount
def flat_discount(price):
    return price - 50
