import matplotlib.pyplot as plt
import numpy as np

beizerPoint = []
lc = None
plt.grid(True)
plt.title(f'Plot of Data Points - Iteration')
plt.xlabel('X')
plt.ylabel('Y')

def getMidPoint(P1, P2):
    return ((P1[0] + P2[0]) / 2), ((P1[1] + P2[1]) / 2)


def PopulateBeizerPoints(ctrl1, ctrl2, ctrl3, nIter, currIter=0):
    if (currIter < nIter):
        midP1 = getMidPoint(ctrl1, ctrl2)
        midP2 = getMidPoint(ctrl2, ctrl3)
        midP3 = getMidPoint(midP1, midP2)

        plt.plot([ctrl1[0], midP1[0], midP2[0], ctrl3[0]], [ctrl1[1], midP1[1], midP2[1], ctrl3[1]], color=lc[currIter], marker='o', linestyle='-')
        
        PopulateBeizerPoints(ctrl1, midP1, midP3, nIter, currIter+1)
        beizerPoint.append(midP3)
        PopulateBeizerPoints(midP3, midP2, ctrl3, nIter, currIter+1)

        plt.pause(0.5)


if __name__ == "__main__":
    x1, y1 = map(float, input('Titik ctrl1: (X Y): ').split())
    x2, y2 = map(float, input('Titik ctrl2: (X Y): ').split())
    x3, y3 = map(float, input('Titik ctrl3: (X Y): ').split())
    nIter = int(input('Banyak iterasi: '))


    lc = [(np.random.random(), np.random.random(), np.random.random()) for i in range(nIter)]

    plt.pause(1)
    plt.plot([x1, x2, x3], [y1, y2, y3], 'bo-')
    plt.pause(0.5)

    for i in range(nIter):
        beizerPoint.append((x1, y1))
        PopulateBeizerPoints((x1, y1), (x2, y2), (x3, y3), i+1)
        beizerPoint.append((x3, y3))

        if i != nIter-1:
            beizerPoint.clear()
    
    plt.plot([point[0] for point in beizerPoint], [point[1] for point in beizerPoint], 'ro-')
    plt.show()