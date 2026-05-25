# Task 5: Mini Program: safe shopping cart

# define empty cart list
cart = []

# loop takes price input from user until chose q
while True:
    # input from user
    price_input = input("Enter the price or 'q' to quit: ")
    # check if user input q to quit
    if price_input == 'q':
        break
    try:
        # convert to flot
        price = float(price_input)
        # chek price is negative or not
        if price < 0 :
            raise Exception("Price is Negative")
        # append price to cart list
        cart.append(price)

    except ValueError:
        print("invalid input")
    except Exception as e:
        print(e)

total_item = len(cart)
total_bill = sum(cart)

print(f"\nTotal items: {total_item}")
print(f"\nTotal Bill: {total_bill}")