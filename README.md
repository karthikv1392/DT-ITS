Here’s a professional and comprehensive **README** file for the updated traffic simulation project:

---

# Traffic Simulation and Digital Twin

This project demonstrates a **real-time traffic simulation** integrated with **machine learning-based predictions** and **dynamic actuation**. The application simulates vehicle movements on a road, predicts traffic conditions near a traffic light, and dynamically controls the light state to optimize traffic flow. The design follows a modular **Digital Twin** architecture, separating simulation components, predictive modeling, and orchestration logic.

---

## Features

### 1. **Traffic Simulation**
- Simulates vehicles moving along a straight road.
- Incorporates characteristics like speed and position for each vehicle.
- Dynamically counts vehicles near the traffic light.

### 2. **Traffic Prediction**
- Uses a **Linear Regression model** trained dynamically during the simulation.
- Predicts the number of vehicles near the traffic light at future time steps.

### 3. **Dynamic Actuation**
- Traffic light state (`RED` or `GREEN`) is controlled in real-time based on predicted traffic conditions.
- Implements rules to optimize traffic flow, e.g., turning green when a predicted threshold is exceeded.

### 4. **Modular Design**
- Separation of concerns with **Vehicle**, **Traffic Light**, **Road**, and **Prediction Model** components.

---

## Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/) for real-time UI and visualization.
- **Backend**: Python for simulation logic and machine learning.
- **Machine Learning**: Scikit-learn for Linear Regression.
- **Visualization**: Plotly for interactive traffic visualization.

---

## Installation

### Prerequisites
- Python 3.7+
- Pip package manager

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/karthikv1392/traffic-simulation.git
   cd traffic-simulation
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run traffic_simulation_app.py
   ```

4. **Access the Application**
   - Open your browser and navigate to: `http://localhost:8501`

---

## Usage

### 1. **Start Simulation**
- Click the **Start Simulation** button to begin real-time traffic simulation.
- Observe:
  - Vehicle movements on the road.
  - Vehicle count near the traffic light.
  - Traffic light state (`RED` or `GREEN`), dynamically updated.

### 2. **Predict Traffic**
- Enter a future time step in the sidebar.
- Click **Predict Traffic** to see the predicted number of vehicles near the traffic light at the specified time.

---

## Architecture Overview

### **Modular Components**

1. **Vehicle Model (`vehicle.py`)**
   - Represents individual vehicles with position and speed characteristics.
   - Handles movement logic based on traffic light state.

2. **Traffic Light Model (`traffic_light.py`)**
   - Manages traffic light state (`RED` or `GREEN`) and timing rules.
   - Updates state based on a configurable cycle duration.

3. **Road Model (`road.py`)**
   - Represents the road and manages all vehicles.
   - Handles vehicle interactions with the traffic light and counts vehicles near it.

4. **Prediction Model (`model.py`)**
   - Trains a Linear Regression model during simulation.
   - Predicts future vehicle counts near the traffic light for dynamic actuation.

5. **Main Script (`traffic_simulation_app.py`)**
   - Orchestrates simulation, prediction, and visualization.
   - Integrates all components for a complete Digital Twin experience.

---

## Application Workflow

1. **Simulation**:
   - Vehicles move dynamically along a road, respecting traffic light states.
   - The simulation collects data on vehicle counts near the traffic light.

2. **Prediction**:
   - A Linear Regression model is trained during the simulation.
   - The model predicts future vehicle counts for a specified time step.

3. **Actuation**:
   - The traffic light state (`RED` or `GREEN`) is updated dynamically based on predictions.
   - Example Rule: Turn `GREEN` if the predicted vehicle count exceeds 5.

4. **Visualization**:
   - Real-time, interactive visualization of:
     - Vehicle positions on the road.
     - Traffic light state.

## Future Enhancements

1. **Advanced Prediction Models**:
   - Replace Linear Regression with time-series models (e.g., ARIMA, LSTMs) for better accuracy.

2. **Multi-Lane and Multi-Light Simulation**:
   - Simulate multiple lanes and intersections with coordinated traffic lights.

3. **Dynamic Vehicle Behavior**:
   - Introduce lane-switching, acceleration/deceleration profiles, and stop-and-go patterns.

4. **Complex Road Networks**:
   - Extend to a grid-like road network with directional movement.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add a new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributors

- **Karthik Vaidhyanathan** - [GitHub Profile](https://github.com/karthikv1392)

---

Feel free to replace the placeholder images with actual screenshots and include the link to the repository. Let me know if you need further refinements! 🚦