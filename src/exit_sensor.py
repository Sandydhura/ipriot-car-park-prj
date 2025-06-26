
import random

from sensor import Sensor


class ExitSensor(Sensor):
   def update_car_park(self, plate):
      self.car_park.remove_car(plate)
      print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

   def _scan_plate(self):
      return random.choice(self.car_park.plates)