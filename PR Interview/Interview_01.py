from abc import ABC, abstractmethod


# ============================================================
# 1. Abstract Base Class
# ============================================================

class Vehicle(ABC):

    # Class variable
    total_vehicles = 0

    def __init__(self, max_speed):
        # TODO 1:
        # Store max_speed as a PRIVATE attribute
        # Example: self.__max_speed = max_speed
        self.__max_speed = max_speed

        # TODO 2:
        # Increment the class variable total_vehicles
        Vehicle.total_vehicles+=1

    # Abstract method
    @abstractmethod
    def drive(self):
        pass

    # TODO 3:
    # Create a getter method called get_max_speed()
    # It should return the private __max_speed
    def get_max_speed(self):
        return self.__max_speed

    # TODO 4:
    # Create a setter method called set_max_speed(new_speed)
    # It should update the private __max_speed
    def set_max_speed(self, new_speed):
        self.__max_speed= new_speed


# ============================================================
# 2. Car Class
# ============================================================

class Car(Vehicle):

    def __init__(self, max_speed, brand):

        # TODO 5:
        # Call the parent class constructor
        # using super()
        super().__init__(max_speed)  

        # TODO 6:
        # Store brand as a PROTECTED attribute
        # Example: self._brand = brand
        self._brand= brand;

    # TODO 7:
    # Override the drive() method
    #
    # Expected format:
    # Car Toyota is driving at 180 km/h
    def drive(self):
         print(
            f"Car {self._brand} is driving at {self.get_max_speed()} km/h"
        )

    # TODO 8:
    # Create get_brand() method
    def get_brand(self):
        return self._brand


# ============================================================
# 3. Bike Class
# ============================================================

class Bike(Vehicle):

    def __init__(self, max_speed, brand):

        # TODO 9:
        # Call the parent class constructor using super()
        super().__init__(max_speed)

        # TODO 10:
        # Store brand as a PROTECTED attribute
        self._brand=brand

    # TODO 11:
    # Override drive()
    #
    # Expected format:
    # Bike Yamaha is driving at 100 km/h
    def drive(self):
        print(f"Bike {self._brand} is driving at {self.get_max_speed()} km/h")

    # TODO 12:
    # Create get_brand()
    def get_brand(self):
        return self._brand


# ============================================================
# 4. Test Code
# ============================================================

if __name__ == "__main__":

    car = Car(180, "Toyota")
    bike = Bike(100, "Yamaha")

    # Polymorphism
    vehicles = [car, bike]

    for vehicle in vehicles:
        vehicle.drive()

    # Class variable
    print(f"Total vehicles: {Vehicle.total_vehicles}")

    # Getter
    print(f"Car max speed: {car.get_max_speed()}")

    # Protected attribute through getter
    print(f"Car brand: {car.get_brand()}")

    # Setter
    car.set_max_speed(200)

    print(f"Updated car max speed: {car.get_max_speed()}")