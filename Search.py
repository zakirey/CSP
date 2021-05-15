import time


def backtracking_search(csp, select_unassigned_variable, order_domain_values, inference):
    start = time.time()
    csp.counter = 0
    solution = backtrack({}, csp, select_unassigned_variable, order_domain_values, inference)
    state_reached = False
    result = dict(solution)
    if (len(result) == len(csp.variables)
            and all(csp.number_of_constraint_conflicts(variables, result[variables], result) == 0 for variables
                    in csp.variables)):
        state_reached = True
    print("Time ", time.time() - start)
    print("Search Counter ", csp.counter)
    assert solution is None or state_reached
    return solution


def backtrack(assignment, csp, select_unassigned_variable,
              order_domain_values, inference):
    csp.counter += 1
    if len(assignment) == len(csp.variables):
        return assignment
    var = select_unassigned_variable(assignment, csp)
    for value in order_domain_values(var, assignment, csp):
        if 0 == csp.number_of_constraint_conflicts(var, value, assignment):
            assignment[var] = value
            if csp.curr_domains is None:
                csp.curr_domains = {v: list(csp.domains[v]) for v in csp.variables}
            removals = [(var, a) for a in csp.curr_domains[var] if a != value]
            csp.curr_domains[var] = [value]
            if inference(csp, var, value, assignment, removals):
                local_solution = backtrack(assignment, csp, select_unassigned_variable,
                                           order_domain_values, inference)
                if local_solution is not None:
                    return local_solution
            for var_r, val_r in removals:
                csp.curr_domains[var_r].append(val_r)
    if var in assignment:
        del assignment[var]
    return None
