class Avenger:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def introduction(self):
        print(f"My name is {self.name}")

class Ironman(Avenger):
    def __init__(self, name, power, weapon):
        super().__init__(name, power)
        self.weapon = weapon
    def show_details(self):
        print(f"i use {self.weapon} as my weapon")

ironman = Ironman("Ironman", "Intelligence", "Suit")
ironman.introduction()
ironman.show_details()
