class Vehicle:
    def __init__(self, id, position, speed):
        """
        Represents a vehicle with position and speed characteristics.
        """
        self.id = id
        self.position = position
        self.speed = speed

    def move(self, road_length):
        """
        Updates the vehicle's position based on its speed and wraps around the road length.
        """
        self.position = (self.position + self.speed) % road_length
