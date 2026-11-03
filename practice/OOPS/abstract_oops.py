from abc import ABC, abstractmethod


class Vechile(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vechile):
    def start(self):
        print("The car start with an ignition key")

    def stop(self):
        print("The Car stops with break pedals")


class ElectricScooter(Vechile):
    def start(self):
        print("Electric Scooter is going with start a power button")

    def stop(self):
        print("Electric Scooter Stop with an electric break")


car = Car()

car.start()