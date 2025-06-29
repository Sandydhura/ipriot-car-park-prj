from abc import ABC, abstractmethod
import  random


class Sensor(ABC):
    def __init__(self, id, is_active=True, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"Sensor {self.id} is {status}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)
