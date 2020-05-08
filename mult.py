from typing import Iterable

class Cycle:
    def __init__(self, data):
        self.data = {}
        self.n = 0
        if (len(data) > 1):
            self.n = max(data)
            last = data[0]
            for x in data[1:]:
                self.data[last] = x
                last = x
            self.data[last] = data[0]

    def __str__(self):
        
        first = min(self.data.keys())
        cur = self.data[first]
        
        s = f"({first}"

        while cur != first:
            s += " " + str(cur)
            cur = self.data[cur]

        s += ")"

        return s

    def __repr__(self):
        return repr(self.data)

def mult(cycles : Iterable [Cycle]):
    
    cycles.reverse()
    
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
            print(cur_number_from, cur_number_to)
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


