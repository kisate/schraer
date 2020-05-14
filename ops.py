from perm import Permutation, Cycle
from typing import Iterable

def mult(perms: Iterable [Permutation]):

    cycles = []
    for x in perms:
        cycles.extend(x.cycles)
    
    return Permutation(mult_c(cycles))

def inverse_c(cycle: Cycle):
    l = cycle.to_list()
    return Cycle(list(reversed(l)))

def inverse(perm: Permutation):
    return Permutation([inverse_c(x) for x in perm.cycles])

def apply(perm: Permutation, points):

    res = []

    for a in points:
        moved = False
        for x in perm.cycles:
            if a in x.data.keys():
                res.append(x.data[a])
                moved = True
        if not moved:
            res.append(a)

    return res

def mult_c(cycles : Iterable [Cycle]):
    
    if (len(cycles) == 0):
        return []

    cycles = list(reversed(cycles))
    
    left = set(range(1, max(cycles, key=lambda x : x.n).n + 1))

    cur_number_from = left.pop()
    cur_number_to = cur_number_from
    cur_cycle = [cur_number_from]
    result = []

    while(len(left) != 0):
        if (cur_number_from == None):
            cur_number_from = left.pop()
            cur_number_to = cur_number_from
            if (len(cur_cycle) > 1):
                result.append(Cycle(cur_cycle))
            cur_cycle = [cur_number_from]

        for cycle in cycles:
            if cur_number_to in cycle.data.keys():
                cur_number_to = cycle.data[cur_number_to]

        if cur_number_to in left:
            if (cur_number_from != cur_number_to):
                cur_cycle.append(cur_number_to)
                cur_number_from = cur_number_to
            left.remove(cur_number_to)
        else:
            cur_number_from = None

    if (len(cur_cycle) > 1):
        result.append(Cycle(cur_cycle))
    
    return result

