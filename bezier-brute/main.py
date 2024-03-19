import time
from matplotlib import pyplot as plt
from plotter import *
from bezier_brute import *

if __name__ == "__main__":
    control_points = []
    N = int(input("Jumlah control points: "))
    for i in range(N):
        inpt  = input(f"Masukkan Control Point {i+1} (X Y): ")
        temp = tuple(map(float, inpt.split(" ")))
        control_points.append(temp)

    N = int(input("Jumlah Titik (semakin banyak semakin mendetail): "))
    time_gap = 5 / N

    start = time.time()
    result = bezier_curve(control_points, N)
    end = time.time()

    for i in range(len(result)):
        plt.plot(
            [result[i][0], result[i + 1][0]],
            [result[i][1], result[i + 1][1]],
            marker="o",
            linestyle="-",
            color="b",
        )
        plt.pause(time_gap)

    plt.clf()
    plt.title("Bezier Curve - Brute Force (de casteljau)")
    plt.xlabel("X", labelpad=20, loc="center", rotation="horizontal")
    plt.ylabel("Y", labelpad=20, loc="center", rotation="vertical")
    plt.plot()
    plot_with_marker(control_points)
    plot_points_as_line(result)
    plt.legend()
    fig = plt.gcf()
    text = "Processing time : " + str(end - start) + " seconds"
    fig.text(0.5, 0.01, text, ha="center", fontsize=12, color="black")

    plt.show()
