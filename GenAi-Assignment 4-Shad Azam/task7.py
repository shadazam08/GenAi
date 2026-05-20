# Task 7: Mini Project- Export Price List

# Create Dicitionary key value pair
price = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

# ask the user input
discount_percentage = int(input("Enter the discount percentage: "))

total_items = len(price)
toata_discount_price = 0

# write the file with write mode
with open('discounted_report.txt', 'w') as f:
    f.write("Product | Original Price | Discounted Price\n")
    # loop the price and product and calculte the discount price and write in file
    for product, orignalPrice in price.items():
        discount_price = orignalPrice - ((orignalPrice * discount_percentage) / 100)
        toata_discount_price += discount_price
        f.write(f"{product} | {orignalPrice} | {discount_price:.2f}\n")

    # Claculate average
    average_discount_price = toata_discount_price / total_items
    f.write(f"Total Items: {total_items}\n")
    f.write(f"Average Discounted Price: {average_discount_price}")


# read file and print the content
with open("discounted_report.txt", 'r') as f:
    content_file = f.read()
    print(content_file)
