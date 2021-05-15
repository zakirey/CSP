# inference methods

def no_inference(csp, var, value, assignment, removals):
    return True


def forward_checking(csp, var, value, assignment, removals):
    for neighbor_var in csp.neighbors[var]:
        if neighbor_var not in assignment:
            for neighbor_val in csp.curr_domains[neighbor_var][:]:
                if not csp.constraints(var, value, neighbor_var, neighbor_val):
                    csp.curr_domains[neighbor_var].remove(neighbor_val)
                    if removals is not None:
                        removals.append((neighbor_var, neighbor_val))
            if not csp.curr_domains[neighbor_var]:
                return False
    return True


def ac3_caller(csp, var, value, assignment, removals):
    return ac3(csp, {(X, var) for X in csp.neighbors[var]}, removals)


def ac3(csp, queue=None, removals=None):
    if queue is None:
        queue = {(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]}
    checks = 0
    while queue:
        (Xi, Xj) = queue.pop()
        revised, checks = revise(csp, Xi, Xj, removals, checks)
        if revised:
            if not csp.curr_domains[Xi]:
                return False, checks
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.add((Xk, Xi))
    return True, checks


def revise(csp, xi, xj, removals, checks=0):
    revised = False
    for x in csp.curr_domains[xi][:]:
        conflict = True
        for y in csp.curr_domains[xj]:
            if csp.constraints(xi, x, xj, y):
                conflict = False
            checks += 1
            if not conflict:
                break
        if conflict:
            csp.curr_domains[xi].remove(x)
            if removals is not None:
                removals.append((xi, x))
            revised = True
    return revised, checks
