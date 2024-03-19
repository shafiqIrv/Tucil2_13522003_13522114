import tkinter as tk
from tkinter import Scrollbar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(0)
import time


# DATA
controlPoints = []
bezierPoints = []
lc = []
nIter = None
N = None
isProcessing = False



def getMidPoint(P1, P2):
    return ((P1[0] + P2[0]) / 2), ((P1[1] + P2[1]) / 2)


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


def quadraticBezier(ctrl1, ctrl2, ctrl3, limIter, currIter=0):
    if (currIter < limIter):
        midP1 = getMidPoint(ctrl1, ctrl2)
        midP2 = getMidPoint(ctrl2, ctrl3)

        midP3 = getMidPoint(midP1, midP2)

        # Left segment
        quadraticBezier(ctrl1, midP1, midP3, limIter, currIter+1)

        bezierPoints.append(midP3)
        
        # Right segment
        quadraticBezier(midP3, midP2, ctrl3, limIter, currIter+1)


def animateQuadraticBezier(ctrl1, ctrl2, ctrl3, limIter, currIter=0):
    if (currIter < limIter):
        midP1 = getMidPoint(ctrl1, ctrl2)
        midP2 = getMidPoint(ctrl2, ctrl3)

        midP3 = getMidPoint(midP1, midP2)

        ax.plot([ctrl1[0], midP1[0], midP2[0], ctrl3[0]], [ctrl1[1], midP1[1], midP2[1], ctrl3[1]], color=lc[currIter], marker='o', linestyle='-')
        
        animateQuadraticBezier(ctrl1, midP1, midP3, limIter, currIter+1)

        bezierPoints.append(midP3)
        
        animateQuadraticBezier(midP3, midP2, ctrl3, limIter, currIter+1)

        fig.canvas.draw_idle()
        fig.canvas.start_event_loop(0.00005)


def NthBezier(controlPoints, limIter, currIter=0):
    if (currIter < limIter):
        midPoints = controlPoints.copy()
        
        left = [controlPoints[0]]
        right = [controlPoints[-1]]


        for i in range(len(controlPoints) -1):
            midMidPoints = []
            for j in range(1, len(midPoints)):
                midMidPoints.append(getMidPoint(midPoints[j], midPoints[j-1]))
            
            left.append(midMidPoints[0])
            right.append(midMidPoints[-1])

            midPoints = midMidPoints
        
        right = right[::-1]

        # LEFT SEGMENT
        NthBezier(left, nIter, currIter+1)

        bezierPoints.append(midPoints[0])

        # RIGHT SEGMENT
        NthBezier(right, nIter, currIter+1)


def animateNthBezier(controlPoints, limIter, currIter=0):
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
                ax.plot(X, Y, marker="o", markerfacecolor=lc[currIter], color="black", ls="-")
            
            left.append(midMidPoints[0])
            right.append(midMidPoints[-1])

            midPoints = midMidPoints
        
        right = right[::-1]

        # LEFT SEGMENT
        animateNthBezier(left, nIter, currIter+1)

        bezierPoints.append(midPoints[0])
        
        # RIGHT SEGMENT
        animateNthBezier(right, nIter, currIter+1)
        fig.canvas.draw_idle()
        fig.canvas.start_event_loop(0.00005)


def clickPoint(event):
    if not isProcessing:
        if event.button == 1:  # Left mouse button click
            x = float("{:.3f}".format(event.xdata))
            y = float("{:.3f}".format(event.ydata))
            if ((x, y) not in controlPoints):
                controlPoints.append((x, y))
                show_plot()
                update_control_points_list()


def show_plot():
    ax.clear()
    EntryPoint.config(text=(str(len(controlPoints))))
    for point in controlPoints:
        ax.plot(point[0], point[1], 'ro')
        ax.text(point[0], point[1], f'({point[0]}, {point[1]})', fontsize=8)
    
    ax.set_title('Click to add points')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    fig.canvas.draw()


def update_control_points_list():
    control_points_list.delete(0, tk.END)
    for i, point in enumerate(controlPoints, start=1):
        control_points_list.insert(tk.END, f"{i}) {point[0]}, {point[1]}")
    

def addTypedPoint():
    try:
        x, y = map(lambda coord: float("{:.3f}".format(float(coord))), EntryAddPoint.get().split())
        if ((x, y) not in controlPoints):
            controlPoints.append((x, y))
            show_plot()
            update_control_points_list()
            EntryAddPoint.delete(0, tk.END)
    except ValueError:
        tk.messagebox.showerror("Error", "Invalid input format. Please enter coordinates in the format 'X Y'.")


def clearControlPoints():
    controlPoints.clear()
    update_control_points_list()
    show_plot()


def runDNC():
    global isProcessing
    isProcessing = True

    BtnAddPoint.config(state='disabled')
    bezierPoints.clear()
    global nIter, lc
    
    nIter = int(EntryIteration.get())

    if (nIter > 0 and len(controlPoints) >= 3):
        lc = [(np.random.random(), np.random.random(), np.random.random()) for i in range(nIter+1)]


        start = time.time()

        if (len(controlPoints) == 3):
            bezierPoints.append(controlPoints[0])
            quadraticBezier(controlPoints[0], controlPoints[1], controlPoints[2], nIter)
            bezierPoints.append(controlPoints[-1])
        else:
            bezierPoints.append(controlPoints[0])
            NthBezier(controlPoints, nIter)
            bezierPoints.append(controlPoints[-1])
        
        end = time.time()
        LabelDNCTimeVal.config(text=f"{(end - start):.10f} s")
        
        ax.clear()

        ax.plot([point[0] for point in controlPoints], [point[1] for point in controlPoints], 'ko-', markerfacecolor='red')

        for point in controlPoints:
            ax.text(point[0], point[1], f'({point[0]}, {point[1]})', fontsize=8)

        ax.plot([point[0] for point in bezierPoints], [point[1] for point in bezierPoints], 'r.-')
        for point in bezierPoints:
            ax.text(point[0], point[1], f'({point[0]:.3f}, {point[1]:.3f})', fontsize=8)

        ax.set_title('Click to add points')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        fig.canvas.draw()

    BtnAddPoint.config(state='normal')

    isProcessing = False


def animateDNC():
    global isProcessing
    isProcessing = True

    BtnAddPoint.config(state='disabled')
    bezierPoints.clear()
    global nIter, lc
    nIter = int(EntryIteration.get())

    if (nIter > 0 and len(controlPoints) >= 3):
        lc = [(np.random.random(), np.random.random(), np.random.random()) for i in range(nIter+1)]

        ax.clear()

        ax.plot([point[0] for point in controlPoints], [point[1] for point in controlPoints], 'ko-', markerfacecolor='red')

        for point in controlPoints:
            ax.text(point[0], point[1], f'({point[0]}, {point[1]})', fontsize=8)
        
        if (len(controlPoints) == 3):
            for i in range(nIter):
                bezierPoints.append(controlPoints[0])
                animateQuadraticBezier(controlPoints[0], controlPoints[1], controlPoints[2], i+1)
                bezierPoints.append(controlPoints[-1])

                if i != nIter-1:
                    bezierPoints.clear()
        else:
            for i in range(nIter):
                bezierPoints.append(controlPoints[0])
                animateNthBezier(controlPoints, i+1)
                bezierPoints.append(controlPoints[-1])

                if i != nIter-1:
                    bezierPoints.clear()
        
        ax.plot([point[0] for point in bezierPoints], [point[1] for point in bezierPoints], 'ro-')
        for point in bezierPoints:
            ax.text(point[0], point[1], f'({point[0]:.3f}, {point[1]:.3f})', fontsize=8)

        ax.set_title('Click to add points')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        fig.canvas.draw()
    
    
    BtnAddPoint.config(state='normal')

    isProcessing = False

def runBF():
    global isProcessing
    isProcessing = True

    BtnAddPoint.config(state='disabled')
    bezierPoints.clear()
    ax.clear()

    N = int(EntryBFIteration.get())

    if (N > 0 and len(controlPoints) >= 3):
        start = time.time()
        result = bezier_curve(controlPoints, N)
        end = time.time()

        LabelBFTimeVal.config(text=f"{(end - start):.10f} s")


        # Plot points
        ax.plot([point[0] for point in result], [point[1] for point in result], 'ro-', markerfacecolor='red')

        # Annotate each point with its coordinates formatted to three decimal places
        for point in result:
            ax.text(point[0], point[1], f'({point[0]:.3f}, {point[1]:.3f})', fontsize=8)

        
        ax.set_title('Click to add points')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        fig.canvas.draw()
    
    BtnAddPoint.config(state='normal')

    isProcessing = False


def animateBF():
    global isProcessing
    isProcessing = True

    BtnAddPoint.config(state='disabled')
    bezierPoints.clear()
    ax.clear()

    N = int(EntryBFIteration.get())

    if (N > 0 and len(controlPoints) >= 3):
        result = bezier_curve(controlPoints, N)

        for i in range(len(result) - 1):
            ax.plot(
                [result[i][0], result[i + 1][0]],
                [result[i][1], result[i + 1][1]],
                'ro-'
            )

            
            ax.text(result[i][0], result[i][1], f'({result[i][0]:.3f}, {result[i][1]:.3f})', fontsize=8)
            fig.canvas.draw_idle()
            fig.canvas.start_event_loop(0.05)
        
        ax.text(result[-1][0], result[-1][1], f'({result[-1][0]:.3f}, {result[-1][1]:.3f})', fontsize=8)

        ax.set_title('Click to add points')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        fig.canvas.draw()


    BtnAddPoint.config(state='normal')
    isProcessing = False


# Initialize tkinter
root = tk.Tk()
root.title('Bezier Curve | 13522003 - 13522114')
root.geometry("1000x700")
custFont = 'Tahoma'

# Initialize plot canvas
fig, ax = plt.subplots()
# ax.set_xlim(-200, 200)
# ax.set_ylim(-200, 200)
fig.canvas.mpl_connect('button_press_event', clickPoint)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(relx=0.35, rely=0.0)

# TKinter Widgets
heading1 = tk.Label(root, text="Bezier Curve Simulator", width=30, bg="#26242f", fg="#FFF", font=(custFont, 15))
heading1.place(x=0, y=0)

LabelEntryPoint = tk.Label(root, text="Number of point: ", font=(custFont, 13))
LabelEntryPoint.place(x=0, y=50)

EntryPoint = tk.Label(root, text="-", font=(custFont, 13))
EntryPoint.place(x=150, y=50)

# Control Points Listbox
control_points_list = tk.Listbox(root, width=25, height=10, font=(custFont, 12))
control_points_list.place(x=0, y=80)

# Scrollbar for Control Points Listbox
scrollbar = Scrollbar(root, orient="vertical", command=control_points_list.yview)
scrollbar.place(x=225, y=80, height=205)

control_points_list.config(yscrollcommand=scrollbar.set)

# Entry add point
LabelAddPoint = tk.Label(root, text="Add new point: ", font=(custFont, 13))
LabelAddPoint.place(x=0, y=300)

EntryAddPoint = tk.Entry(root, width=17, font=(custFont, 12))
EntryAddPoint.place(x=120, y=300)

BtnAddPoint = tk.Button(root, text="add", font=(custFont, 10), command=addTypedPoint)
BtnAddPoint.place(x=250, y=330)

BtnClearControlPoint = tk.Button(root, text="clear", font=(custFont, 10), command=clearControlPoints)
BtnClearControlPoint.place(x=250, y=250)


# DnC
LabelDNC = tk.Label(root, text="Divide & Conquer", font=(custFont, 13))
LabelDNC.place(x=400, y=500)

# Entry iteration
LabelEntryIteration = tk.Label(root, text="Number of iteration: ", font=(custFont, 13))
LabelEntryIteration.place(x=350, y=530)

EntryIteration = tk.Entry(root, width=5, font=(custFont, 12))
EntryIteration.place(x=510, y=530)

BtnRunDNC = tk.Button(root, text="Run", font=(custFont, 10), command=runDNC)
BtnRunDNC.place(x=450, y=570)

LabelDNCTime = tk.Label(root, text="Execution time: ", font=(custFont, 11))
LabelDNCTime.place(x=350, y=610)

LabelDNCTimeVal = tk.Label(root, text="-", font=(custFont, 11))
LabelDNCTimeVal.place(x=470, y=610)


BtnAnimateDNC = tk.Button(root, text="Animate", font=(custFont, 10), command=animateDNC)
BtnAnimateDNC.place(x=440, y=640)


# Bruteforce
LabelBF = tk.Label(root, text="Brute Force", font=(custFont, 13))
LabelBF.place(x=720, y=500)

# Entry N Point
LabelEntryBFIteration = tk.Label(root, text="Number of Iteration: ", font=(custFont, 13))
LabelEntryBFIteration.place(x=650, y=530)

EntryBFIteration = tk.Entry(root, width=5, font=(custFont, 12))
EntryBFIteration.place(x=840, y=530)

BtnRunBF = tk.Button(root, text="Run", font=(custFont, 10), command=runBF)
BtnRunBF.place(x=750, y=570)

LabelBFTime = tk.Label(root, text="Execution time: ", font=(custFont, 11))
LabelBFTime.place(x=650, y=600)

LabelBFTimeVal = tk.Label(root, text="-", font=(custFont, 11))
LabelBFTimeVal.place(x=770, y=600)

BtnAnimateBF = tk.Button(root, text="Animate", font=(custFont, 10), command=animateBF)
BtnAnimateBF.place(x=740, y=630)

root.mainloop()
