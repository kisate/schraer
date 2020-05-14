from perm import Permutation
from ops import apply, mult, inverse
from typing import Iterable
from tree import Tree, build_tree

class FullStabilizerChain:
    def __init__(self, n, base, s, trees : Iterable[Tree]):
        self.base = base
        self.n = n
        self.s = s
        self.trees = trees
        super().__init__()

    def calc_size(self):
        size = 1
        for t in self.trees:
            size *= len(t.orbit)
        
        return size


def check_belongs(chain : FullStabilizerChain, val : Permutation, step = 0):

    if (step == len(chain.base)):
        return (val == Permutation([]), [])
    
    b = chain.base[step]

    u = apply(val, [b])[0]

    if u not in chain.trees[step].orbit:
        return (False, [])
    
    node = chain.trees[step].node_dict[u]

    new_val = val

    cert = []

    while u != b:
        
        new_val = mult([node.perm, new_val])
        u = apply(node.perm, [u])[0]

        cert.append(inverse(node.perm))

        node = node.parent
    
    res = check_belongs(chain, new_val, step + 1)

    cert.extend(res[1])

    return (res[0], cert)

def make_gens(tree: Tree, S : Iterable[Permutation]):
    newS = []

    for s in S:
        for u in tree.orbit:
            hu = tree.get_h_u(u)
            hsu = tree.get_h_u(apply(s, [u])[0])
            newp = mult([inverse(hsu), s, hu])
            if newp not in newS:
                newS.append(newp)
    
    return newS

def normalize(S : Iterable[Permutation]):
    newS = []

    n = max(S, key=lambda x : x.n).n

    base = [{} for _ in range(n)]

    for s in S:
        for x in range(1, n + 1):
            u = apply(s, [x])[0]
            if u != x:
                if u in base[x-1]:
                    s = mult([inverse(s), base[x-1][u]])
                else:
                    base[x-1][u] = s
                    if s not in newS:
                        newS.append(s)
                    break
    
    return newS

def build_chain(S : Iterable[Permutation]):
    n = max(S, key=lambda x : x.n).n

    b = 1

    ans = []

    while S:
        tree = build_tree(b, S)
        ans.append(tree)
        S = normalize(make_gens(tree, S))
        b += 1

    return FullStabilizerChain(n, list(range(1, b + 1)), S, ans)

def check_chain(b, base, s : Iterable[Permutation], trees : Iterable[Tree]):
    