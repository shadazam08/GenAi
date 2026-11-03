# Task 7:   Mini Project: Simple Inventory System (OOP only)

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ₹{self.price}")
        print(f"Category: {self.category}")

    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    def __add__(self, other):
        return self.price + other.price


class Inventory:
    def __init__(self):
        self.products = [] 

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                return

    def get_total_value(self):
        return sum(product.price for product in self.products)

    def show_all_products(self):
        print("All Products")
        for product in self.products:
            print(product)
        print("-" * 30)


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self, product):
        self.inventory.add_product(product)

    def show_summary(self):
        print(f"Store Summary")
        print(f"Total Items in Inventory: {len(self.inventory.products)}")
        print(f"Total Inventory Value: {self.inventory.get_total_value()}")
        print("-" * 30)


my_store = Store("Tech World Store")

product1 = Product("Laptop", 45000, "Electronics")
product2 = Product("Mouse", 1200, "Accessories")
product3 = Product("Keyboard", 2500, "Accessories")

my_store.add_new_product(product1)
my_store.add_new_product(product2)
my_store.add_new_product(product3)

my_store.inventory.show_all_products()

my_store.show_summary()

combined_price = product1 + product2
print(f"Combined price of : {combined_price}")
