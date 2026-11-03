# Task 3: Inheritance (Single-level)

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_info(self):
        print(f"The product name is : {self.name}")
        print(f"The product category is : {self.category}")
        print(f"The product price is : {self.__price}")
        print("-" * 30)


class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    def get_info(self):
        super().get_info()
        print(f"Warranty Period : {self.warranty_years} years")


my_laptop = ElectronicProduct("Gaming Laptop", 75000, "Electronics", 2)
my_laptop.get_info()
