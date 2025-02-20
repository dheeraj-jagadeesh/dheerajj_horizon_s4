# TASK 4

Develop a ROS 2 project using a publisher and subscriber. The project can be a messaging
app, a game, or any other creative implementation. The more complex and impressive
the project, the better.

I have created a differential drive robot and simulated it using Gazebo

## Installation & Setup
Ensure you have the necessary dependencies installed before running the projects.

### Prerequisites (UBUNTU 22.04)
- ROS 2 Humble  
- Python 3.10.12 (Latest Version is Preferred)
- Colcon build system  
- Gazebo Classic
- teleop_twist_keyboard (ROS 2)

### Setup
```sh
# Clone the repository
git clone https://github.com/dheeraj-jagadeesh/dheerajj_horizon_s4.git

# 1) IN A NEW TERMINAL
source /opt/ros/humble/setup.bash

# 2) Navigate to the project directory
cd dheerajj_horizon_s4/task4

# 3) Build the workspace 
colcon build

# 4) Source the workspace
source install/setup.bash

# 5) To launch the Gazebo Model
ros2 launch mobile_dd_robot gazebo_model.launch.py

# 6) Open a New Terminal 
source /opt/ros/humble/setup.bash

cd dheerajj_horizon_s4/task4

source install/setup.bash


# 7) To control the Robot
ros2 run teleop_twist_keyboard teleop_twist_keyboard

(Follow the instructions that show up to control the movement of the Robot)

```