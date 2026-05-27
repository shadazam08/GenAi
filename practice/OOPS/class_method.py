class Avengers:
    origin = "Avenger"
    def __init__(self,name,power):
        self.name = name
        self.power = power
    @classmethod
    def origin_info(cls):
        print(f"All avengers are from {cls.origin}")
    def self_info(self):
        print(f"My name is {self.name} and my power is {self.power}")

ironman = Avengers("Ironman", "Intelligence")
ironman.self_info()
ironman.origin_info()