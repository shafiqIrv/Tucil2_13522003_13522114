from matplotlib import pyplot as plt


def initialize():
    plt.title("Bezier Curve")
    plt.xlabel("X-axis label", labelpad=20, loc="center", rotation="horizontal")
    plt.ylabel("Y-axis label", labelpad=20, loc="center", rotation="vertical")


def plot_points_as_line(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.plot(x, y, linestyle="-", color="r")
