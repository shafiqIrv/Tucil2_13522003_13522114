bezierPoints = []
iter = 5


def MidPoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]


def PopulateBezierPoints(ctrl1, ctrl2, ctrl3, currIter):
    if currIter < iter:
        midPoint1 = MidPoint(ctrl1, ctrl2)
        midPoint2 = MidPoint(ctrl2, ctrl3)
        midPoint3 = MidPoint(midPoint1, midPoint2)
        currIter += 1

        PopulateBezierPoints(ctrl1, midPoint1, midPoint3, currIter)
        bezierPoints.append(midPoint3)
        PopulateBezierPoints(midPoint3, midPoint2, ctrl3, currIter)


def CreateBezier(ctrl1, ctrl2, ctrl3, N):
    bezierPoints = []
    bezierPoints
    PopulateBezierPoints(ctrl1, ctrl2, ctrl3, 0)
    bezierPoints.append(ctrl3)
