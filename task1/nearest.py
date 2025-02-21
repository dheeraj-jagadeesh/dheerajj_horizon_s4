import matplotlib.pyplot as plt

# This function is used get user input for points
def get_points():
    points = []
    numpoints = int(input("Enter the number of points? "))

    for i in range(numpoints):
        x = int(input(f"Enter point x{i+1} = "))
        y = int(input(f"Enter point y{i+1} = "))
        points.append((x, y))
    
    return points

# This is used to calculate distance
def calc_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# This is used to find and draw lines to the nearest neighbors
def draw_the_line(points):
    used_edgings = set()
    plt.figure()
    unique_points = set(points)
    x_points = []
    y_points = []
    for point in points:
        x_points.append(point[0])
        y_points.append(point[1])
    plt.scatter(x_points, y_points,color = "red", zorder=2)

    i = 0
    for point in points:
        distances = []
        j = 0
        for next_point in points:
            if i != j:
                dist = calc_distance(point, next_point)
                distances.append((dist, j))
            j += 1
        distances.sort()
            


        # Finding the nearest neighbor that hasn't been connected with a duplicate edge
        for dist, neighbour in distances:
            edging = tuple(sorted((i, neighbour)))
            if edging not in used_edgings:
                used_edgings.add(edging)
                plt.plot([point[0], points[neighbour][0]],
                         [point[1], points[neighbour][1]], 'b-', zorder=1)
                break  # Move to the next point after finding the nearest unused neighbor
        i += 1

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Nearest Neighbor Plot')
    plt.show()

# Main function
def main():
    points = get_points()
    draw_the_line(points)

if __name__ == '__main__':
    main()