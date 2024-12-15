import pandas as pd
from sklearn.linear_model import LinearRegression

class TrafficPredictionModel:
    def __init__(self):
        """
        Manages training and predictions for traffic conditions near the light.
        """
        self.model = None
        self.data = []

    def update_data(self, time, vehicle_count):
        """
        Updates the dataset with the current time step and vehicle count.
        """
        self.data.append({"time": time, "count": vehicle_count})

    def train(self):
        """
        Trains the Linear Regression model dynamically using the latest data.
        """
        if len(self.data) < 2:  # Minimum 2 data points to train
            return False
        df = pd.DataFrame(self.data)
        X = df["time"].values.reshape(-1, 1)
        y = df["count"].values
        self.model = LinearRegression().fit(X, y)
        return True

    def predict(self, future_time):
        """
        Predicts the vehicle count near the traffic light at a future time.
        """
        if self.model is None:
            return 0
        prediction = self.model.predict([[future_time]])
        return max(0, int(prediction[0]))  # Ensure non-negative predictions
