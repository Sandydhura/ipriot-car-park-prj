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

    def update_displays(self):
        message = "{available_bays or FULL}"
        for display in self.displays:
            display.update(message)

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self):
        ...

    def remove_car(self):
        ...
