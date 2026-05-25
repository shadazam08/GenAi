# Task 2: Bill Calculator with Error Handling

# list of price
prices = [120, 350, 'abc', 500, -200, 800]
running_total = 0
for price in prices:
    try:
        # chek price is number or not
        if not isinstance(price, int):
            raise TypeError("Value is not a number")
        # check price is negative or not
        if price < 0:
            raise ValueError("Negative Price not alloewd")
        # calculate running total
        running_total += price
        print(f"Running Total: {running_total}")
    except ValueError as ve:
        print(f"{ve}")
    except TypeError as te:
        print(f"{te}")
