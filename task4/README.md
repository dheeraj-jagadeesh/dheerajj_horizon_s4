# **TASK 4**  

This project simulates a **differential drive robot** in **Gazebo Classic** using **ROS 2 Humble**. The robot can be controlled via the **teleop_twist_keyboard** package.  

## **Installation & Setup**  

Ensure you have the necessary dependencies installed before running the project.  

### **Prerequisites** (Ubuntu 22.04)  

- ROS 2 **Humble**  
- Python **3.10.12** (Latest version is preferred)  
- **Colcon** build system  
- **Gazebo Classic**  
- **teleop_twist_keyboard** (ROS 2)  

---

## **Setup Instructions**  

### **1. Clone the Repository**  

```sh
git clone https://github.com/dheeraj-jagadeesh/dheerajj_horizon_s4.git
```

---

### **2. Build and Source the Workspace**  

#### **Open a new terminal and run:**  

```sh
# Source ROS 2 Humble
source /opt/ros/humble/setup.bash

# Navigate to the project directory
cd dheerajj_horizon_s4/task4

# Build the workspace
colcon build

# Source the workspace
source install/setup.bash
```

---

### **3. Launch the Gazebo Model**  

```sh
ros2 launch mobile_dd_robot gazebo_model.launch.py
```

---

### **4. Control the Robot using Keyboard Teleoperation**  

#### **Open a new terminal and run:**  

```sh
# Source ROS 2 Humble
source /opt/ros/humble/setup.bash

# Navigate to the project directory
cd dheerajj_horizon_s4/task4

# Source the workspace
source install/setup.bash

# Run the teleoperation node
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

📌 **Follow the on-screen instructions to control the robot’s movement.**  

---

## **Project Structure**  

```
dheerajj_horizon_s4/
│── task4/
│   ├── src/                 # Source code for the robot model
│   ├── launch/              # Launch files for simulation
│   ├── config/              # Configuration files
│   ├── install/             # Compiled package binaries
│   ├── setup.py             # Package setup file
│   ├── README.md            # Project documentation
```

---

