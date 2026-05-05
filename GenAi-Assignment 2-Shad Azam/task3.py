# Task 3: user Menu (while loop + break / continue)

orders =[]
while True:
    print("\nMenu:")
    print("1. Add Order Amount")
    print("2. Show all orders and totals after applied discounts")
    print("q. Exit\n")
    # Get user choice
    choice = input("Enter your choice: ")
    
    if choice == '1':
        try:
            order_amount = int(input("Enter the order amount: "))
            orders.append(order_amount)
        except ValueError:
            print("Invalid input. Please enter a numeric value for the order amount.")
    elif choice == '2':
        if not orders:
            print("No orders to display.")
        else:
            total=0
            print(f"Order Amount\tDiscount%\tFinal amount")
            # print("Current orders:")
            for order_amount in orders:
                # 3 - discount rules
                if order_amount >= 2000:
                    discount_rate = 0.15
                elif 1500 <= order_amount < 2000:
                    discount_rate = 0.10
                elif 1000 <= order_amount < 1500:
                    discount_rate = 0.07
                else:
                    discount_rate = 0.0

                # 4 - calculate final price
                discount = order_amount * discount_rate
                final_amount  = order_amount - discount
                total += final_amount
                    
                print(f"{order_amount}\t\t{int(discount_rate*100)}%\t\t{final_amount}")
            print(f"\nTotal amount after discounts: {total}")
            
    elif choice == 'q':
        print("\nExiting the program. Goodbye!") 
        break
    else:
        print("\nInvalid Input.")
        continue