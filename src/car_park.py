from display import Display
from sensor import Sensor


class CarPark:
    def __init__(self, location="Unknown", capacity=100, plates=None, displays=None):
        self.sensors = None
        self.location = location
        self.capacity = capacity
        self.plates = plates or []         # List of car plate numbers
        self.displays = displays or []     # List of Display objects


    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))

    def update_displays(self):
        data = {
            "available_bays": self.available_bays,
            "temperature": 25,
            "location": self.location
        }

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        if plate in self.plates:
            print(f"Car {plate} is already parked.")
        else:
            self.plates.append(plate)
            self.update_displays()

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
        else:
            raise ValueError(f"Car {plate} not found.")

