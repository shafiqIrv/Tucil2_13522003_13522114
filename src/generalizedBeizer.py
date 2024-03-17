import matplotlib.pyplot as plt
import numpy as np

beizerPoint = []
plt.title(f'Plot of Data Points - Iteration')
plt.xlabel('X')
plt.ylabel('Y')

def getMidPoint(P1, P2):
    return ((P1[0] + P2[0]) / 2), ((P1[1] + P2[1]) / 2)


def PopulateBeizerPoints(controlPoints, limIter, currIter=0):
    if (currIter < limIter):
        midPoints = controlPoints.copy()
        
        left = [controlPoints[0]]
        right = [controlPoints[-1]]


        for i in range(len(controlPoints) -1):
            midMidPoints = []
            for j in range(1, len(midPoints)):
                midMidPoints.append(getMidPoint(midPoints[j], midPoints[j-1]))
            
            
            if i == 0:
                X = [controlPoints[0][0]] + [point[0] for point in midMidPoints] + [controlPoints[-1][0]]
                Y = [controlPoints[0][1]] + [point[1] for point in midMidPoints] + [controlPoints[-1][1]]
                plt.plot(X, Y, color=lc[currIter], marker='o', linestyle='-')            
            
            left.append(midMidPoints[0])
            right.append(midMidPoints[-1])

            midPoints = midMidPoints
        
        right = right[::-1]

        # LEFT SEGMENT
        PopulateBeizerPoints(left, nIter, currIter+1)
        beizerPoint.append(midPoints[0])
        # RIGHT SEGMENT
        PopulateBeizerPoints(right, nIter, currIter+1)

        plt.pause(0.00005)


if __name__ == "__main__":
    N = int(input('Banyak titik kontrol: '))
    controlPoints = []

    for i in range(N):
        x, y = map(float, input('Titik ctrl1: (X Y): ').split())
        controlPoints.append((x, y))
    
    nIter = int(input('Banyak iterasi: '))
    lc = [(np.random.random(), np.random.random(), np.random.random()) for i in range(nIter+1)]

    plt.pause(1)
    plt.plot(
        [x[0] for x in controlPoints],
        [y[1] for y in controlPoints],
        'bo-'
    )
    plt.pause(0.5)


    for i in range(nIter):
        beizerPoint.append(controlPoints[0])
        PopulateBeizerPoints(controlPoints, i+1)
        beizerPoint.append(controlPoints[-1])

        if i != nIter-1:
            beizerPoint.clear()
    
    plt.plot([point[0] for point in beizerPoint], [point[1] for point in beizerPoint], 'ro-', linewidth=5)
    print(beizerPoint)
    plt.show()