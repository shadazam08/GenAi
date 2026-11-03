# Task 2: Constructor & Encapsulation

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

    def get_price(self):
        print(f"The product price is : {self.__price}")

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            return self.get_price()
        else:
            return f"The new price is not greter the zero"
        


    def apply_discount(self, percent):
        discount_amount = (self.__price * percent) / 100
        final_price = self.__price - discount_amount
        return final_price

product = Product("Gaming Laptop", 40000, "Electronics")

product.get_info()

product.set_price(450000)