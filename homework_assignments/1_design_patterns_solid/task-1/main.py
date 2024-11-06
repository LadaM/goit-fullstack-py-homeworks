from factory_pattern import EUVehicleFactory

if __name__ == '__main__':

    vehicle1 = EUVehicleFactory.create_car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = EUVehicleFactory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()