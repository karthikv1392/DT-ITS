from vehicle import Vehicle
class Road:
    def __init__(self, length, num_vehicles, vehicle_speed):
        """
        Represents a road with vehicles and traffic lights.
        """
        self.length = length
        self.vehicles = [
            Vehicle(id=i, position=(i * (length / num_vehicles)), speed=vehicle_speed)
            for i in range(num_vehicles)
        ]

    def move_vehicles(self, traffic_light):
        """
        Moves vehicles along the road, stopping them if they're near a red traffic light.
        """
        for vehicle in self.vehicles:
            if traffic_light.state == "RED" and abs(vehicle.position - traffic_light.position) < 50:
                vehicle.speed = 0  # Stop vehicle near red light
            else:
                vehicle.speed = 20  # Reset to normal speed
            vehicle.move(self.length)

    def count_near_traffic_light(self, traffic_light, radius=50):
        """
        Counts the number of vehicles near the traffic light within the given radius.
        """
        return sum(1 for vehicle in self.vehicles if abs(vehicle.position - traffic_light.position) < radius)
