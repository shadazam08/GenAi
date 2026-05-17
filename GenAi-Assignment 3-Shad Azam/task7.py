# Task 7: Mini Problem: Menu Using Functions

# add price function
def add_price(price_list, price):
    price_list.append(price)
    print(f"Price {price} added to the list.")  

# average price function
def get_average_price(price_list):
    if len(price_list) == 0:
        print("No prices in the list")
        return None
    avg = sum(price_list) / len(price_list)
    return avg

# Max price function
def get_max_price(price_list):
    if len(price_list) == 0:
        print("No prices in the list")
        return None
    max_price = max(price_list)
    return max_price


# Menu 
prices_list = []
while True:
    print("\nMenu:")
    print("1. Add Price")
    print("2. Show Average Price")
    print("3. Show Highest Price")
    print("q. Quit\n")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        try:
            price = float(input("Enter the price: "))
            add_price(prices_list, price)
        except ValueError:
            print("Invalid input. Please enter a numeric value for the price.")
    elif choice == '2':
        average_price = get_average_price(prices_list)
        if average_price is not None:
            print(f"The average price is: {average_price:.2f}")
    elif choice == '3':
        max_price = get_max_price(prices_list)
        if max_price is not None:
            print(f"The maximum price is: {max_price:.2f}")
    elif choice == 'q':
        print("\n Goodbye!") 
        break
    else:
        print("\nInvalid Input.")
        continue
