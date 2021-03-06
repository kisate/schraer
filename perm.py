from typing import Iterable, List, Dict

class Cycle:
    def __init__(self, data : Iterable[int]):
        self.data = {}
        self.n = 0
        if (len(data) > 1):
            self.n = max(data)
            last = data[0]
            for x in data[1:]:
                self.data[last] = x
                last = x
            self.data[last] = data[0]

    def to_list(self):

        l = []

        if (self.n > 0):
            first = min(self.data.keys())
            cur = self.data[first]

            l.append(first)

            while cur != first:
                l.append(cur)
                cur = self.data[cur]

        return l

    def __str__(self):
        
        p = " ".join([str(x) for x in self.to_list()])

        s = f"({p})"

        return s

    def __repr__(self):
        return repr(self.data)

    def __eq__(self, value):
        return self.data.__eq__(value.data)

    def __hash__(self):
        return hash(str(self))

class Permutation:
    def __init__(self, cycles : Iterable [Cycle]):
        self.cycles = cycles
        self.n = 0
        if (len(cycles) > 0):
            self.n = max(cycles, key=lambda x : x.n).n

    def __str__(self):
        return " ".join([str(c) for c in self.cycles])
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, value):
        return self.cycles == value.cycles

    def __hash__(self):
        return hash(tuple(self.cycles))


def to_perm(*cycles):
    return Permutation([Cycle(x) for x in cycles])

def build_perm(data : Dict[int, int]):
    n = max(data.keys())
    cycles = []

    been = set()

    for i in range(1, n + 1):  
        if i not in been and data[i] != i:
            cycle = [i]
            cur = data[i]
            been.add(i)
            while cur != i:
                been.add(cur)
                cycle.append(cur)
                cur = data[cur]
            cycles.append(Cycle(cycle))

    return Permutation(cycles)
