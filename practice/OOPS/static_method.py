class Avengers:
    @staticmethod
    def mission():
        print("All Avengers have a mission to protect the world from threats.")
    origin = "Avenger"
    def __init__(self, name, power):
        self.name = name
        self.power = power
    @classmethod
    def origin_info(cls):
        print(f"All avengers are from {cls.origin}")
    def introduction(self):
        print(f"My name is {self.name} and my power is {self.power}")

ironman = Avengers("Ironman", "Intelligence")
ironman.introduction()
ironman.mission()
ironman.origin_info()