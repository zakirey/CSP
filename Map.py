import math
import random as rd
from MapInterface import GUI
from shapely.geometry import LineString
from CSP import CSP
from Search import backtracking_search


def intersect(x1, y1, x2, y2):
    if x1 == x2 or x1 == y2 or y1 == x2 or y1 == y2:
        return False
    return LineString([x1, y1]).intersects(LineString([x2, y2]))


def map_coloring_csp(points_number, width, height, line_distance, var_heuristics, val_heuristics, inference):
    coordinates = []
    for _ in range(points_number):
        point = [rd.randint(1, width), rd.randint(1, height)]
        if point not in coordinates:
            coordinates.append(point)
    coordinates = [[x * line_distance, y * line_distance] for x, y in coordinates]

    gui = GUI(width, height, line_distance)
    gui.draw_background()

    lines = []
    for _ in range(3):
        rd.shuffle(coordinates)
        for X in coordinates:
            distance_sort = sorted(coordinates, key=lambda p: math.dist(p, X))
            for Y in distance_sort[1:]:
                if [X, Y] in lines or [Y, X] in lines:
                    continue
                if any(map(lambda x: intersect(X, Y, *x), lines)):
                    continue
                gui.draw_line(*X, *Y)
                lines.append([X, Y])
                break

    neighbors = {str(c): [] for c in coordinates}
    for [start, end] in lines:
        if str(start) in neighbors:
            neighbors[str(start)].append(str(end))
            neighbors[str(end)].append(str(start))

    colors = ['red', 'blue', 'green', 'black']
    domains = {str(c): [] for c in neighbors.keys()}
    for key in neighbors.keys():
        domains[str(key)] = colors

    def different_values_constraint(var1, a, var2, b):
        return a != b

    map_csp = CSP(list(neighbors.keys()), domains, neighbors, different_values_constraint)
    solution = backtracking_search(map_csp, select_unassigned_variable=var_heuristics,
                                   order_domain_values=val_heuristics,
                                   inference=inference)
    gui.draw_color_points(coordinates, [x for x in solution.values()])

    gui.root.mainloop()
