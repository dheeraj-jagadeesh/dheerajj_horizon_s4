import matplotlib.pyplot as plt

# Function to get user input for points
def get_points():
    points = []
    n = int(input("Enter the number of points: "))
    for i in range(n):
        x, y = map(float, input(f"Enter coordinates for point {i + 1} (x y): ").split())
        points.append((x, y))
    return points

# Function to calculate distance
def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# Function to find and draw lines to the nearest neighbors
def draw_nearest_neighbors(points):
    used_edges = set()
    plt.figure()
    plt.scatter([p[0] for p in points], [p[1] for p in points], color='red', zorder=5)

    for i, point in enumerate(points):
        distances = []
        for j, other_point in enumerate(points):
            if i != j:
                dist = euclidean_distance(point, other_point)
                distances.append((dist, j))

        distances.sort()  # Sort by distance

        # Find the nearest neighbor that hasn't been connected with a duplicate edge
        for dist, neighbor_idx in distances:
            edge = tuple(sorted((i, neighbor_idx)))
            if edge not in used_edges:
                used_edges.add(edge)
                plt.plot([point[0], points[neighbor_idx][0]],
                         [point[1], points[neighbor_idx][1]], 'b-', zorder=1)
                break  # Move to the next point after finding the nearest unused neighbor

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Nearest Neighbor Plot')
    plt.show()

# Main function
def main():
    points = get_points()
    draw_nearest_neighbors(points)

if __name__ == '__main__':
    main()