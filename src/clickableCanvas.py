import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class ClickHandler:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.points = []
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.clear_button = Button(plt.axes([0.81, 0.025, 0.1, 0.04]), 'Clear')
        self.clear_button.on_clicked(self.clear_points)
        self.show_plot()

    def onclick(self, event):
        if event.button == 1:  # Left mouse button click
            if -200 <= event.xdata <= 200 and -200 <= event.ydata <= 200:
                self.points.append((event.xdata, event.ydata))
                self.show_plot()

    def clear_points(self, event):
        self.points = []
        self.show_plot()

    def show_plot(self):
        self.ax.clear()
        for point in self.points:
            self.ax.plot(point[0], point[1], 'ro')  # Plotting points as red circles
            self.ax.text(point[0], point[1], f'({point[0]:.2f}, {point[1]:.2f})', fontsize=8)
        self.ax.set_title('Click to add points')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_xlim(-200, 200)  # Set x-axis limits
        self.ax.set_ylim(-200, 200)  # Set y-axis limits
        self.fig.canvas.draw()

    def get_points(self):
        return self.points

if __name__ == "__main__":
    click_handler = ClickHandler()
    # plt.xlim(-200, 200)
    # plt.ylim(-200, 200)
    plt.show()