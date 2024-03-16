import matplotlib.pyplot as plt


def plot_points_as_line(points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    plt.figure()
    plt.plot(x_values, y_values, marker="o", linestyle="-")
    plt.title("Points Plotted as Line")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


import matplotlib.pyplot as plt


def plot_points_as_curve(points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    plt.figure()
    plt.plot(x_values, y_values, marker="o", linestyle="-", color="b")
    plt.title("Points Plotted as Curve")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
