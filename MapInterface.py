import tkinter as tk

RADIUS = 5


class GUI:
    def __init__(self, width, height, line_distance):
        self.width = width
        self.height = height
        self.line_distance = line_distance
        self.root = tk.Tk()
        self.root.title('Map Solution')
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=(1 + width) * line_distance, height=(1 + height) * line_distance,
                                bg="#fff")
        self.canvas.pack()
        self.root.update()

    def draw_background(self):
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                self.draw_circle(i * self.line_distance, j * self.line_distance, color='#eee')

    def draw_circle(self, x, y, radius=RADIUS, color='#000'):
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline='')

    def draw_line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, fill="#242424")

    def draw_color_points(self, coordinates, colors):
        for point, color in zip(coordinates, colors):
            self.draw_circle(*point, color=color)
