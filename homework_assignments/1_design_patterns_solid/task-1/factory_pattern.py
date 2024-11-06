from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_car(make, model) -> Car:
        pass

    @staticmethod
    @abstractmethod
    def create_motorcycle(make, model) -> Motorcycle:
        pass


class EUVehicleFactory(VehicleFactory):
    @staticmethod
    def create_car(make, model) -> Car:
        return Car(make, model, "EU Spec")

    @staticmethod
    def create_motorcycle(make, model) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


class USVehicleFactory(VehicleFactory):
    @staticmethod
    def create_car(make, model) -> Car:
        return Car(make, model, "US Spec")

    @staticmethod
    def create_motorcycle(make, model) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")
