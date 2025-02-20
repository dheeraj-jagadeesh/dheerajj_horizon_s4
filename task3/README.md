# TASK 3

Create a ROS 2 publisher node to publish a topic and a subscriber node to receive and
print the published values.


## Installation & Setup
Ensure you have the necessary dependencies installed before running the projects.

### Prerequisites
- ROS 2 Humble  
- Python 3.10.12 (Latest Version is Preferred)
- Colcon build system  

### Setup
```sh
# Clone the repository
git clone https://github.com/dheeraj-jagadeesh/dheerajj_horizon_s4.git

# 1) IN A NEW TERMINAL
source /opt/ros/humble/setup.bash

# 2) Navigate to the project directory
cd dheerajj_horizon_s4/task3

# 3) Build the workspace 
colcon build

# 4) Source the workspace
source install/setup.bash

# 5) To see the Publisher node
ros2 run ente_nodes publisher_node

# 6) Open a New Terminal 
Repeat steps 1 to 4

# 7) To see the Subscribe node
ros2 run ente_nodes subscriber_node

```
# Screenshots

## Publisher

![image alt](https://github.com/dheeraj-jagadeesh/dheerajj_horizon_s4/blob/28d121ce4b4495dafe793902b2dd821b0930ce59/task3/images/publisher.png)

## Subscriber

![image alt](https://github.com/dheeraj-jagadeesh/dheerajj_horizon_s4/blob/28d121ce4b4495dafe793902b2dd821b0930ce59/task3/images/subscriber.png)
