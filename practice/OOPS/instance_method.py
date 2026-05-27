class Avengers:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def show_details(self):
        print(f"My name is {self.name} and my power is {self.power}")

ironman = Avengers("Ironman", "Intelligence")
ironman.show_details()