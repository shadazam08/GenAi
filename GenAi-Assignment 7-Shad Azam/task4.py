# Task 4: Polymorphism

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_info(self):
        print(f"The product name is : {self.name}")
        print(f"The product price is : {self.__price}")
        print(f"The product category is : {self.category}")
        print("-" * 30)

    def get_price(self):
        return self.__price


class Laptop(Product):
    def __init__(self, name, price, category, ram_size):
        super().__init__(name, price, category)
        self.ram_size = ram_size

    def get_info(self):
        print(f"Laptop Name: {self.name} ")
        print(f"RAM: {self.ram_size} ")
        print(f"Price: {self.get_price()} ")
        print("-" * 30)

class Mobile(Product):
    def __init__(self, name, price, category, battery):
        super().__init__(name, price, category)
        self.battery = battery

    def get_info(self):
        print(f"Mobile Name: {self.name} ")
        print(f"Battery: {self.battery} ")
        print(f"Price: {self.get_price()} ")

laptop = Laptop("Dell Inspiron", 55000, "Electronics", "16GB")
mobile = Mobile("iPhone 15", 70000, "Electronics", "3349 mAh")

products_list = [laptop, mobile]

for product in products_list:
    product.get_info()