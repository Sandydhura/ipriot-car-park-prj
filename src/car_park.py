class CarPark:
    def __init__(self, location="Unknown", capacity=100, plates=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []         # List of car plate numbers
        self.displays = displays or []     # List of Display objects

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

