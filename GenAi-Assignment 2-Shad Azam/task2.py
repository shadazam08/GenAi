# Task 2: Process Multiple Orders (for loop)

# 1 - List the number of orders to process
orders = [1200, 2500, 800, 1750, 3000]

# 2 - Initialize total revenue and discounted orders count
total_revenue = 0
discounted_orders = 0
print(f"Order Amount\tDiscount%\tFinal amount")

# 3 - Loop through each order and apply the same discount rules
for order_amount in orders:
    # 4 - discount rules
    if order_amount >= 2000:
        discount_rate = 0.15
    elif 1500 <= order_amount < 2000:
        discount_rate = 0.10
    elif 1000 <= order_amount < 1500:
        discount_rate = 0.07
    else:
        discount_rate = 0.0

    # 5 - calculate final price
    discount = order_amount * discount_rate
    final_amount  = order_amount - discount
    # Extra: number of orders that  received a discount (discount_rate > 0)
    if discount_rate > 0:
        discounted_orders += 1
    # calcultae total revenue after discount
    total_revenue += final_amount
    
    print(f"{order_amount}\t\t{int(discount_rate*100)}%\t\t{final_amount}")

# print total revenue and number of discounted orders
print(f"\nTotal Revenue after discounts: {total_revenue}")
print(f"Number of discount orders: {discounted_orders}")
    