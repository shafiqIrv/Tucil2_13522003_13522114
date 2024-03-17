def de_casteljau(control_points, t):
    if len(control_points) == 1:
        return control_points[0]
    else:
        new_points = []
        for i in range(len(control_points) - 1):
            x = (1 - t) * control_points[i][0] + t * control_points[i + 1][0]
            y = (1 - t) * control_points[i][1] + t * control_points[i + 1][1]
            new_points.append((x, y))
        return de_casteljau(new_points, t)


def bezier_curve(control_points, n):
    curve = []
    for t in [i / n for i in range(n + 1)]:
        curve.append(de_casteljau(control_points, t))
    return curve
