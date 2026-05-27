class Avenger:
    def __init__(self,name,power, weapon):
        self.name = name
        self.power = power
        self.weapon = weapon
    def introduction(self):
        print(f"My name is {self.name} and my power is {self.power} and my weapon is {self.weapon}")
    def carrying_weapon(self):
        print(f"i am carrying the weapon {self.weapon}")

ironman = Avenger("Ironman", "Intelligence", "Suit")
ironman.introduction()
ironman.carrying_weapon()

    