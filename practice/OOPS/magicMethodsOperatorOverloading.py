class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"The product name is : {self.name}")
        print(f"The product price is : {self.price}")
        print(f"The product category is : {self.category}")

    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    def __add__(self, other):
        return self.price + other.price


product1 = Product("Laptop", 40000, "electronic")
product2 = Product("Mouse", 1500, "electronic")


print(product1)
print(product2)

total_price = product1 + product2

print(f"Total Combined Price: {total_price}")

