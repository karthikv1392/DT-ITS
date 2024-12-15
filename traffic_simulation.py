import streamlit as st
import numpy as np
import pandas as pd
import time
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

# Traffic Simulation Parameters
road_length = 500  # Length of the road in meters
num_vehicles = 10  # Number of vehicles
vehicle_speed = 20  # Average speed in m/s

# Global simulation data to store results
if "simulation_data" not in st.session_state:
    st.session_state.simulation_data = []
if "model" not in st.session_state:
    st.session_state.model = None

# Initialize Vehicle Positions
vehicle_positions = np.linspace(0, road_length, num=num_vehicles, endpoint=False)

# Traffic Light States
traffic_light = {"state": "GREEN", "position": 250, "cycle": 10}  # At position 250

# Actuation: Adjust vehicle speeds based on traffic light
def adjust_speed(position, speed, light_state):
    if light_state == "RED" and abs(position - traffic_light["position"]) < 50:
        return 0  # Stop the vehicle near the red light
    return speed

# Count vehicles near the traffic light
def count_near_traffic_light(positions, light_position, radius=50):
    return sum(1 for pos in positions if abs(pos - light_position) < radius)

# Train the model dynamically
def train_dynamic_model():
    # Convert simulation data to a DataFrame
    df = pd.DataFrame(st.session_state.simulation_data)
    if df.empty:
        return None
    # Prepare data for training
    X = df["time"].values.reshape(-1, 1)  # Time as feature
    y = df["count"].values  # Vehicle count as target
    # Train the model
    model = LinearRegression().fit(X, y)
    return model

# Predict future traffic
def predict_traffic(model, future_time):
    if model is None:
        return 0
    prediction = model.predict([[future_time]])
    return max(0, int(prediction[0]))  # Ensure non-negative counts

# Simulate Traffic
def simulate_traffic():
    global vehicle_positions
    for t in range(40):  # Simulate 30 time steps
        time.sleep(0.5)
        new_positions = []
        for i, pos in enumerate(vehicle_positions):
            speed = adjust_speed(pos, vehicle_speed, traffic_light["state"])
            pos += speed * (1 + np.random.uniform(-0.1, 0.1))  # Add randomness
            pos = pos % road_length  # Wrap around the road
            new_positions.append(pos)

        vehicle_positions[:] = new_positions
        vehicle_count = count_near_traffic_light(vehicle_positions, traffic_light["position"])
        st.session_state.simulation_data.append({"time": t, "count": vehicle_count, "positions": vehicle_positions.copy()})

        # Train the model dynamically with the latest data
        st.session_state.model = train_dynamic_model()

        # Actuation based on prediction
        future_count = predict_traffic(st.session_state.model, t + 5)  # Predict 5 steps ahead
        if future_count > num_vehicles // 2:  # Example rule: More than half the vehicles
            traffic_light["state"] = "GREEN"
        else:
            traffic_light["state"] = "RED"

        yield t, vehicle_positions, traffic_light["state"], vehicle_count

# Streamlit UI
st.title("Traffic Flow Digital Twin")
st.sidebar.header("Simulation Controls")

# Display real-time updates at the top
status_placeholder = st.empty()

# Initialize session state for the plot
if "figure" not in st.session_state:
    st.session_state.figure = go.Figure(
        layout=go.Layout(
            title="Real-Time Traffic Simulation",
            xaxis_title="Road Position (m)",
            yaxis_title="Vehicles",
            xaxis=dict(range=[0, road_length]),
            yaxis=dict(range=[-1, 1]),
        )
    )

# Simulation
if st.sidebar.button("Start Simulation"):
    st.write("### Real-Time Traffic Simulation")
    fig = st.session_state.figure

    # Create a placeholder for the plot
    plot_placeholder = st.empty()

    for t, positions, light_state, vehicle_count in simulate_traffic():
        # Clear the previous traces and add updated data
        fig.data = []  # Clear previous traces
        fig.add_trace(
            go.Scatter(
                x=positions,
                y=[0] * len(positions),
                mode="markers",
                marker=dict(size=10, color="blue"),
                name="Vehicles",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=[traffic_light["position"]],
                y=[0],
                mode="markers",
                marker=dict(
                    size=20,
                    color="green" if light_state == "GREEN" else "red",
                    symbol="triangle-up",
                ),
                name=f"Traffic Light ({light_state})",
            )
        )

        # Update the plot in the placeholder
        plot_placeholder.plotly_chart(fig, use_container_width=True)

        # Update real-time status at the top
        status_placeholder.write(f"**Time Step**: {t}, **Vehicles near Traffic Light**: {vehicle_count}, **Light State**: {light_state}")

# Prediction
future_time = st.sidebar.number_input("Future Time Step", min_value=1, max_value=100, value=10)
if st.sidebar.button("Predict Traffic"):
    if "model" not in st.session_state or st.session_state.model is None:
        st.warning("The model is not yet trained. Start the simulation to train dynamically.")
    else:
        prediction = predict_traffic(st.session_state.model, future_time)
        st.write(f"Predicted vehicles near the traffic light at time {future_time}: {prediction}")
