# Heuristics for variable ordering
def first_unassigned_variable(assignment, csp):
    return next(iter([var for var in csp.variables if var not in assignment]), None)


def mrv(assignment, csp):
    return min([v for v in csp.variables if v not in assignment],
               key=lambda var: num_legal_values(csp, var, assignment))


def num_legal_values(csp, var, assignment):
    if csp.curr_domains:
        return len(csp.curr_domains[var])
    else:
        return sum(map(bool, (csp.number_of_constraint_conflicts(var, val, assignment) == 0 for val in csp.domains[var])
                       ))


# Heuristics for value ordering
def unordered_domain_values(var, assignment, csp):
    return (csp.curr_domains or csp.domains)[var]


def lcv(var, assignment, csp):
    return sorted((csp.curr_domains or csp.domains)[var], key=lambda val: csp.number_of_constraint_conflicts(var, val,
                                                                                                             assignment)
                  )
