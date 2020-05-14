from perm import Permutation, Cycle
from ops import apply, mult, inverse
from typing import Iterable, Dict

class Node:
    def __init__(self, parent, perm : Permutation, val):
        self.parent = parent
        self.perm = perm
        self.val = val
        self.children = []

    def __str__(self):
        
        return f"{self.val} {self.perm} [{' '.join([str(x) for x in self.children])}]"

class Tree:
    def __init__(self, root : Node, orbit, node_dict : Dict[int, Node], S : Iterable[Permutation]):
        self.root = root
        self.orbit = orbit
        self.node_dict = node_dict
        self.S = S

    def __str__(self):
        return self.root.__str__()

    def get_h_u(self, u):

        assert(u in self.orbit)

        h = Permutation([])
        node = self.node_dict[u]
        while node.val != self.root.val:
            h = mult([node.perm, h])
            node = node.parent
        
        return inverse(h)

#Построить бамбук Шраера-Симса

def build_tree(b, perms : Iterable [Permutation]):

    root = Node(None, Permutation([]), b)
    node_dict = {b : root}

    if (len(perms) == 0):
        return Tree(root, set([b]), node_dict, perms)

    q = [(b, root)]
    orbit = set([b])
    cur_node = root

    while (len(q) > 0):
        cur_elem, cur_node = q.pop(0)
        for p in perms:
            next_elem = apply(p, [cur_elem])[0]
            while next_elem not in orbit:
                node = Node(cur_node, inverse(p), next_elem)
                cur_node.children.append(node)
                node_dict[next_elem] = node

                q.append((next_elem, node))
                orbit.add(next_elem)
                next_elem = apply(p, [cur_elem])[0]

    return Tree(root, orbit, node_dict, perms)
