class Dog:
    def __init__(self):
        self.name = "Tommy"
        self.breed = "Labrador"
        self.color = "Black"
    def show_info(self):
        print(f"this dog is {self.name} and its breed is {self.breed} and its color is {self.color}")

dog1 = Dog()
dog1.show_info()