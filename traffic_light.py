class TrafficLight:
    def __init__(self, position, cycle_duration=10):
        """
        Represents a traffic light with a position and a duration for each state (RED/GREEN).
        """
        self.position = position
        self.cycle_duration = cycle_duration
        self.state = "GREEN"
        self.time_in_state = 0

    def update(self):
        """
        Updates the traffic light's state based on its cycle duration.
        """
        self.time_in_state += 1
        if self.time_in_state >= self.cycle_duration:
            self.state = "RED" if self.state == "GREEN" else "GREEN"
            self.time_in_state = 0
