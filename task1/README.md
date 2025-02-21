# Nearest Neighbour Plotter

This Python program allows users to input a set of points and visualize the nearest neighbour connections between them. It uses the `matplotlib` library to plot the points and draw lines to their nearest neighbours.

## Dependencies

The following dependencies are required to run the program:

- Python 3.x
- matplotlib

## Installation

### Windows

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install matplotlib**:
   - Open Command Prompt.
   - Run the following command:
     ```
     pip install matplotlib
     ```

### Ubuntu

1. **Install Python**:
   - Open Terminal.
   - Run the following commands:
     ```
     sudo apt update
     sudo apt install python3
     sudo apt install python3-pip
     ```

2. **Install matplotlib**:
   - Run the following command:
     ```
     pip3 install matplotlib
     ```

## Usage

To run the program, follow these steps:

1. **Open a terminal or command prompt**.
2. **Navigate to the directory** where the program file is located.
3. **Run the program** using the following command:
     ```
     python3 nearest.py
     ```

4. **How to Run the Program**

- Run the script in a terminal or command prompt.

- Enter the number of points when prompted.

- Input the coordinates (x, y) for each point.

- The program will display a scatter plot with lines connecting each point to its nearest unused neighbour.

## Example

**Input:**

- Enter the number of points? 5
- Enter point x1 = 2
- Enter point y1 = 3
- Enter point x2 = 5
- Enter point y2 = 7
- Enter point x3 = 8
- Enter point y3 = 2
- Enter point x4 = 1
- Enter point y4 = 6
- Enter point x5 = 6
- Enter point y5 = 5

**Output:**

A plotted graph with red dots representing the input points and blue lines connecting each point to its nearest neighbour.

**Notes**

Duplicate points are allowed, but duplicate edges are avoided.

Ensure matplotlib is installed before running the script.

