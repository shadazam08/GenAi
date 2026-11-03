# Task 1: Basic Class & Object Creation

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"The product name is : {self.name}")
        print(f"The product category is : {self.category}")
        print(f"The product price is : {self.price}")
        print("-" * 30)

    def apply_discount(self, percent):
        discount_amount = (self.price * percent) / 100
        final_price = self.price - discount_amount
        return final_price


product1 = Product("Gaming Laptop", 185000, "Electronics")
product2 = Product("Gaming Desktop", 145000, "Electronics")

product1.get_info()
product2.get_info()

discounted_price1 = product1.apply_discount(5)
discounted_price2 = product2.apply_discount(5)
print(f"Discounted Price of Gaming Laptop: {discounted_price1}")
print(f"Discounted Price of Gaming Desktop: {discounted_price2}")