class Grandparent:
    def __init__(self, nationality, baldness, anger_issue):
        self.nationality = nationality
        self.baldness = baldness
        self.anger_issue = anger_issue
    
    def introduction(self):
        print(f"Hello my nationality is : {self.nationality} and about my baldness : {self.baldness} and about my anger issue : {self.anger_issue}")


class Parent(Grandparent):
    def __init__(self, nationality, baldness, anger_issue, intelligence):
        super().__init__(nationality, baldness, anger_issue)
        self.intelligence = intelligence

    def intelligence_details(self):
        print(f"About my intelligence if you guys want to know that whether if i am itelligent or not then the answre is : {self.intelligence}")
    
class Child(Parent):
    def __init__(self, nationality, baldness, anger_issue, intelligence, charm):
        super().__init__(nationality, baldness, anger_issue, intelligence)
        self.charm = charm

    def charm_details(self):
        print(f"About my charm if you guys want to know that whether if i am charming or not then the answer is : {self.charm}")


parent = Parent("Indian", "Yes", "No", "Yes")
child = Child("Indian", "No", "Yes", "Yes", "Yes")
parent.introduction()
child.introduction()