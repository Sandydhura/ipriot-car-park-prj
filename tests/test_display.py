import unittest
from display import Display
from car_park import CarPark

class TestDisplay (unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Main Street", 50)
        self.display = Display(1, "Welcome to the car park", True)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertTrue(self.display.is_on)

    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")

    if __name__ == "__main__":
        unittest.main()