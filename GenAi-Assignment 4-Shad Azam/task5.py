# Task 5: Create Product into File(user input)

# add a list to stroe the user input 3 product and price using for loop in range(3)
products = []
for i in range(3):
    product_name = input("Enter the ProductName: ")
    product_price = input("Enter the price: ")
    # append the product and price in products list
    products.append(f"{product_name} | {product_price}\n")

# open the file with write mode
with open("products.txt", "w") as f:
    # write the header
    f.write("ProductName | Price\n")
    # write the products and price 
    f.writelines(products)
# open the file read mode
with open("products.txt", "r") as f:
    content = f.read()
    print(content)

