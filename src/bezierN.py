from plotting import *

main = []

plt.figure()
plt.title("Points Plotted as Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)


def middle(coor1, coor2, N):

    x = coor1[0] + (coor2[0] - coor1[0]) * N
    y = coor1[1] + (coor2[1] - coor1[1]) * N
    plt.plot(x, y, marker="o", linestyle="-", color="b")
    # if coor2[0] > coor1[0]:
    #     x = coor1[0] + coor2[0] * N
    # else:
    #     x = coor1[0] - coor2[0] * N

    # if coor2[1] > coor1[1]:
    #     y = coor1[1] + coor2[1] * N

    # else:
    #     y = coor1[1] - coor2[1] * N
    return [x, y]


def calculate(list, N):
    if len(list) > 1:
        temp = []
        for i in range(len(list) - 1):
            temp.append(middle(list[i], list[i + 1], N))
        print("Temp", temp)
        calculate(temp, N)

        main.insert(0, list[0])
        print("Inserted", list[0])
        plt.plot(list[0][0], list[0][1], marker="o", linestyle="-", color="r")

        # plt.pause(0.5)

        main.append(list[-1])
        print("Appended", list[-1])
        plt.plot(list[-1][0], list[-1][1], marker="o", linestyle="-", color="g")
        # plt.pause(0.5)


list = [[0, 0], [2, 4], [6, 4], [8, 0], [15, 3]]

i = 0.01
calculate(list, 0.5)
while i <= 1:
    calculate(list, i)
    i += 0.01
    plt.pause(0.02)
plt.show()
# plot_points_as_curve(main)
