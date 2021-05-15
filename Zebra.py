from ZebraInterface import GUI
from CSP import CSP
from Search import backtracking_search


def zebra_problem_csp(var_heuristics, val_heuristics, inference):
    colors = ['Red', 'Yellow', 'Blue', 'Green', 'Ivory']
    pets = ['Dog', 'Fox', 'Snails', 'Horse', 'Zebra']
    beverage = ['OrangeJuice', 'Tea', 'Coffee', 'Milk', 'Water']
    nationality = ['Englishman', 'Spaniard', 'Norwegian', 'Ukrainian', 'Japanese']
    cigarettes = ['Kools', 'Chesterfields', 'OldGold', 'LuckyStrike', 'Parliaments']
    variables = colors + pets + beverage + nationality + cigarettes
    domains = {}
    for var in variables:
        domains[var] = list(range(1, 6))

    neighbors = {'Englishman': ['Red'], 'Red': ['Englishman'],
                 'Spaniard': ['Dog'], 'Dog': ['Spaniard'],
                 'Coffee': ['Green'], 'Green': ['Coffee', 'Ivory'],
                 'Ukrainian': ['Tea'], 'Tea': ['Ukrainian'],
                 'Ivory': ['Green'], 'Yellow': ['Kools'],
                 'OldGold': ['Snails'], 'Snails': ['OldGold'],
                 'Kools': ['Horse', 'Yellow'], 'Horse': ['Kools'],
                 'Chesterfields': ['Fox'], 'Fox': ['Chesterfields'],
                 'LuckyStrike': ['OrangeJuice'], 'OrangeJuice': ['LuckyStrike'],
                 'Japanese': ['Parliaments'], 'Parliaments': ['Japanese'],
                 'Norwegian': ['Blue'], 'Blue': ['Norwegian'],
                 'Zebra': [], 'Water': [], 'Milk': []}

    for part in [colors, pets, beverage, nationality, cigarettes]:
        for A in part:
            for B in part:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)

    domains['Norwegian'] = [1]
    domains['Milk'] = [3]

    def zebra_constraint(var1, a, var2, b, recurse=0):
        same = (a == b)
        next_to = abs(a - b) == 1
        if var1 == 'Englishman' and var2 == 'Red':
            return same
        if var1 == 'Spaniard' and var2 == 'Dog':
            return same
        if var1 == 'Chesterfields' and var2 == 'Fox':
            return next_to
        if var1 == 'Norwegian' and var2 == 'Blue':
            return next_to
        if var1 == 'Kools' and var2 == 'Yellow':
            return same
        if var1 == 'OldGold' and var2 == 'Snails':
            return same
        if var1 == 'LuckyStrike' and var2 == 'OrangeJuice':
            return same
        if var1 == 'Ukrainian' and var2 == 'Tea':
            return same
        if var1 == 'Japanese' and var2 == 'Parliaments':
            return same
        if var1 == 'Kools' and var2 == 'Horse':
            return next_to
        if var1 == 'Coffee' and var2 == 'Green':
            return same
        if var1 == 'Green' and var2 == 'Ivory':
            return a - 1 == b
        if recurse == 0:
            return zebra_constraint(var2, b, var1, a, 1)
        if ((var1 in colors and var2 in colors) or (var1 in pets and var2 in pets) or
                (var1 in beverage and var2 in beverage) or (var1 in nationality and var2 in nationality) or
                (var1 in cigarettes and var2 in cigarettes)):
            return not same
        raise Exception('Variable is incorrect or missing')

    zebra_csp = CSP(variables, domains, neighbors, zebra_constraint)
    solution = backtracking_search(zebra_csp, select_unassigned_variable=var_heuristics,
                                   order_domain_values=val_heuristics,
                                   inference=inference)

    house1 = []
    house2 = []
    house3 = []
    house4 = []
    house5 = []
    for key, value in zip(solution.keys(), solution.values()):
        if value == 1:
            house1.append(key)
        if value == 2:
            house2.append(key)
        if value == 3:
            house3.append(key)
        if value == 4:
            house4.append(key)
        if value == 5:
            house5.append(key)

    houses = [house1, house2, house3, house4, house5]
    gui = GUI()
    gui.print(houses)
    gui.root.mainloop()
