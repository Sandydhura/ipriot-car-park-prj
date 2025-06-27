import unittest
from entry_sensor import EntrySensor
from exit_sensor import  ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Unknown", 100)
        self.entry = EntrySensor(id=1, is_active=True, car_park=self.car_park)
        self.exit = ExitSensor(id=2, is_active=True, car_park=self.car_park)

    def test_entry_sensor_init(self):
        self.assertEqual(self.entry.id, 1)
        self.assertTrue(self.entry.is_active)
        self.assertEqual(self.entry.car_park.location, "Unknown")

    def test_exit_sensor_init(self):
        self.assertEqual(self.exit.id, 2)
        self.assertTrue(self.exit.is_active)
        self.assertEqual(self.exit.car_park.location, "Unknown")

    def test_entry_sensor_adds_plate(self):
        self.entry.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 1)

    if __name__ == "__main__":
        unittest.main()