from bezier import *
from plotting import *

# Create a Bezier curve
p1 = input("Enter the first control point: ")
p1 = tuple(map(float, p1.split(",")))

p2 = input("Enter the second control point: ")
p2 = tuple(map(float, p2.split(",")))

p3 = input("Enter the third control point: ")
p3 = tuple(map(float, p3.split(",")))

i = int(input("Enter the number of Iterations: "))
iter = i
CreateBezier(p1, p2, p3, i)

plot_points_as_curve(bezierPoints)
