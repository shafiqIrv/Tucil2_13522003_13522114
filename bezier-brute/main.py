import time
from matplotlib import pyplot as plt
from plotter import *
from bezier_brute import *

if __name__ == "__main__":
    control_points = [(20, 10), (45, 70), (70, 35), (90, 80), (10, 60)]
    N = 300
    time_gap = 5 / N
    start = time.time()
    result = bezier_curve(control_points, N)
    end = time.time()

    for i in range(len(result) - 1):
        plt.plot(
            [result[i][0], result[i + 1][0]],
            [result[i][1], result[i + 1][1]],
            marker="o",
            linestyle="-",
            color="b",
        )
        plt.pause(time_gap)

    plt.clf()
    plt.title("Points Plotted as Curve")
    plt.xlabel("X-axis label", labelpad=20, loc="center", rotation="horizontal")
    plt.ylabel("Y-axis label", labelpad=20, loc="center", rotation="vertical")
    plot_points_as_line(result)
    fig = plt.gcf()
    text = "Processing time : " + str(end - start) + " seconds"
    fig.text(0.5, 0.01, text, ha="center", fontsize=12, color="black")

    plt.show()
