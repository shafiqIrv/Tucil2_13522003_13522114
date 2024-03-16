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


def PopulateBeizerPoints(ctrl1, ctrl2, ctrl3, ctrl4, nIter, currIter=0):
    if (currIter < nIter):
        midP1 = getMidPoint(ctrl1, ctrl2)
        midP2 = getMidPoint(ctrl2, ctrl3)
        midP3 = getMidPoint(ctrl3, ctrl4)

        midP4 = getMidPoint(midP1, midP2)
        midP5 = getMidPoint(midP2, midP3)

        # plt.plot([ctrl1[0], midP1[0], midP2[0], midP3[0], ctrl4[0]], [ctrl1[1], midP1[1], midP2[1], midP3[1], ctrl4[1]], color=lc[currIter], marker='o', linestyle='-')
        
        PopulateBeizerPoints(ctrl1, midP1, midP4, midP2, nIter, currIter+1)
        beizerPoint.append(midP4)
        beizerPoint.append(midP5)
        PopulateBeizerPoints(midP2, midP5, midP3, ctrl4, nIter, currIter+1)

        plt.pause(0.5)


if __name__ == "__main__":
    x1, y1 = map(float, input('Titik ctrl1: (X Y): ').split())
    x2, y2 = map(float, input('Titik ctrl2: (X Y): ').split())
    x3, y3 = map(float, input('Titik ctrl3: (X Y): ').split())
    x4, y4 = map(float, input('Titik ctrl4: (X Y): ').split())
    nIter = int(input('Banyak iterasi: '))
    lc = [(np.random.random(), np.random.random(), np.random.random()) for i in range(nIter)]



    plt.pause(1)
    plt.plot([x1, x2, x3, x4], [y1, y2, y3, y4], 'bo-')
    plt.pause(0.5)

    for i in range(nIter):
        beizerPoint.append((x1, y1))
        PopulateBeizerPoints((x1, y1), (x2, y2), (x3, y3), (x4, y4), i+1)
        beizerPoint.append((x4, y4))

        if i != nIter-1:
            beizerPoint.clear()
    
    print(beizerPoint, len(beizerPoint))
    plt.plot([point[0] for point in beizerPoint], [point[1] for point in beizerPoint], 'ro-')
    plt.show()