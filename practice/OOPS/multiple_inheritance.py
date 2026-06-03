class Ironman:
    def __init__(self, name, power, suit, weapon, nationality="American"):
        self.name = name
        self.power = power
        self.suit = suit
        self.weapon = weapon
        self.nationality = nationality
    
    def introduction(self):
        print(f"Hello my name is : {self.name} and my power is : {self.power} and my suit is : {self.suit} and my weapon is : {self.weapon} and my nationality is : {self.nationality}")

class CaptanAmerica:
    def __init__(self, name, power, suit, weapon, nationality="American"):
        self.name = name
        self.power = power
        self.suit = suit
        self.weapon = weapon
        self.nationality = nationality
    
    def weapon_details(self):
        print(f"Hello my name is : {self.name} and my weapon is : {self.weapon}")
    
class Hulk(Ironman, CaptanAmerica):
    def __init__(self, name, power, suit, weapon, nationality, angre_issue):
        super().__init__(name, power, suit, weapon, nationality)
        self.angre_issue = angre_issue
    
    def anger_issue_details(self):
        print(f"Hello my name is : {self.name} and about my anger issue : {self.angre_issue}")

hulk = Hulk("Hulk", "Super Strength", "Mark 85 Iron Man Suit", "Replulsor, become and shield ", "American", "Yes")
hulk.introduction()
hulk.weapon_details()
hulk.anger_issue_details()