class GrandParent:
    def __init__(self, name, locker_key):
        self.name = name
        self._locker_key = locker_key
    # getter method

    def locker_info(self):
        print(f"The Locker key info is : {self._locker_key}")


class Parent(GrandParent):
    def __init__(self, name, locker_key):
        super().__init__(name, locker_key)

    def child_revals(self):
        print(f"The Locker key information is : {self._locker_key}")


grandPa = GrandParent("Azam", "1234567")
grandPa.locker_info()

parent = Parent("Shad", "1234567")

parent.child_revals()


# print(dir(grandPa))
