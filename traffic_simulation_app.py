import time
import streamlit as st
import plotly.graph_objects as go
from road import Road
from traffic_light import TrafficLight
from model import TrafficPredictionModel

# Initialize simulation components
road = Road(length=500, num_vehicles=10, vehicle_speed=20)
traffic_light = TrafficLight(position=250)
prediction_model = TrafficPredictionModel()

# Streamlit UI
st.title("Traffic Simulation and Digital Twin")
st.sidebar.header("Simulation Controls")

# Real-time status
status_placeholder = st.empty()

# Initialize session state for plot
if "figure" not in st.session_state:
    st.session_state.figure = go.Figure(
        layout=go.Layout(
            title="Real-Time Traffic Simulation",
            xaxis_title="Road Position (m)",
            yaxis_title="Vehicles",
            xaxis=dict(range=[0, road.length]),
            yaxis=dict(range=[-1, 1]),
        )
    )

# Simulation
if st.sidebar.button("Start Simulation"):
    st.write("### Real-Time Traffic Simulation")
    fig = st.session_state.figure

    # Create placeholder for plot
    plot_placeholder = st.empty()

    for t in range(30):  # Simulate 30 time steps
        time.sleep(0.5)

        # Update traffic light state
        traffic_light.update()

        # Move vehicles and count near traffic light
        road.move_vehicles(traffic_light)
        vehicle_count = road.count_near_traffic_light(traffic_light)

        # Update prediction model data and train dynamically
        prediction_model.update_data(time=t, vehicle_count=vehicle_count)
        prediction_model.train()

        # Predict future vehicle count
        future_count = prediction_model.predict(future_time=t + 5)

        # Dynamic actuation based on prediction
        if future_count > 5:  # Example: Turn green if more than 5 vehicles are predicted
            traffic_light.state = "GREEN"
        else:
            traffic_light.state = "RED"

        # Update plot
        fig.data = []  # Clear previous traces
        fig.add_trace(
            go.Scatter(
                x=[vehicle.position for vehicle in road.vehicles],
                y=[0] * len(road.vehicles),
                mode="markers",
                marker=dict(size=10, color="blue"),
                name="Vehicles",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=[traffic_light.position],
                y=[0],
                mode="markers",
                marker=dict(
                    size=20,
                    color="green" if traffic_light.state == "GREEN" else "red",
                    symbol="triangle-up",
                ),
                name=f"Traffic Light ({traffic_light.state})",
            )
        )
        plot_placeholder.plotly_chart(fig, use_container_width=True)

        # Update status at the top
        status_placeholder.write(
            f"**Time Step**: {t}, **Vehicles near Light**: {vehicle_count}, "
            f"**Future Predicted Vehicles**: {future_count}, **Light State**: {traffic_light.state}"
        )

# Prediction
future_time = st.sidebar.number_input("Future Time Step", min_value=1, max_value=100, value=10)
if st.sidebar.button("Predict Traffic"):
    prediction = prediction_model.predict(future_time)
    st.write(f"Predicted vehicles near the traffic light at time {future_time}: {prediction}")
