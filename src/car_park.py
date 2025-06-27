from display import Display
from sensor import Sensor
from pathlib import Path
from datetime import datetime

class CarPark:
    def __init__(self, location="Unknown", capacity=100, plates=None, displays=None, log_file=Path("log.txt")):
        self.sensors = None
        self.location = location
        self.capacity = capacity
        self.plates = plates or []         # List of car plate numbers
        self.displays = displays or []     # List of Display objects
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)


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
            self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
            self._log_car_activity(plate, "entered")
        else:
            raise ValueError(f"Car {plate} not found.")

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now()}\n")

