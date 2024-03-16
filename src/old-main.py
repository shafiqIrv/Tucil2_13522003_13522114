import matplotlib.pyplot as plt

nIter = None
beizerPoint = []

def getMidPoint(P1, P2):
    return [((P1[0] + P2[0]) / 2), ((P1[1] + P2[1]) / 2)]


def PopulateBeizerPoints(ctrl1, ctrl2, ctrl3, currIter=0):
    if (currIter < nIter):
        midP1 = getMidPoint(ctrl1, ctrl2)
        midP2 = getMidPoint(ctrl2, ctrl3)
        midP3 = getMidPoint(midP1, midP2)

        plt.plot([midP1[0], midP3[0], midP2[0]], [midP1[1], midP3[1], midP2[1]], 'bo-')

        # plt.grid(True)
        
        PopulateBeizerPoints(ctrl1, midP1, midP3, currIter+1)
        beizerPoint.append(midP3)
        PopulateBeizerPoints(midP3, midP2, ctrl3, currIter+1)
        plt.pause(1)


if __name__ == "__main__":
    x1, y1 = map(float, input('Titik ctrl1: (X Y): ').split())
    x2, y2 = map(float, input('Titik ctrl2: (X Y): ').split())
    x3, y3 = map(float, input('Titik ctrl3: (X Y): ').split())
    nIter = int(input('Banyak iterasi: '))

    plt.plot([x1, x2, x3], [y1, y2, y3], 'bo-')

    beizerPoint.append((x1, y1))
    PopulateBeizerPoints((x1, y1), (x2, y2), (x3, y3))
    beizerPoint.append((x3, y3))


    print(beizerPoint)
    plt.plot([point[0] for point in beizerPoint], [point[1] for point in beizerPoint], 'bo-')
    plt.title('Bezier Curve with {} Iterations'.format(nIter))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()