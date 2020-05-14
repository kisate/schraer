from ops import apply, inverse, mult
from perm import *
from tree import build_tree
from chain import make_gens, normalize, build_chain

def test_apply():
    p = Permutation([Cycle([1,2,3])])
    print(apply(p, [1]))
    print(apply(p, [2]))
    print(apply(p, [3]))
    print(apply(p, [1, 2]))
    print(apply(p, [1, 2, 4, 3]))
    print(apply(p, [1, 2, 3]))
    print(apply(p, [4]))
    print(apply(p, [4,5]))
    print(apply(p, [4,5,6, 1]))

def test_inverse():
    print(inverse(to_perm([1,2,3])))
    print(inverse(to_perm([1,2,3], [4,5])))
    print(inverse(to_perm([1,2,3], [4,5,6,7])))
    print(inverse(to_perm([1,2,3], [4,5,6,7], [8,9,12])))

def test_build():
    print(build_tree(7, [to_perm([1,2,3]), to_perm([3,4,5]), to_perm([5,6,7,8]), to_perm([4,5]), to_perm([9, 10])]))

def test_mult():
    print(mult([to_perm([1,2]), to_perm([1,2])]))
    print(Permutation([]))
    print(mult([to_perm([1,2]), to_perm([1,2])]) == Permutation([]))
    print(mult([to_perm([1,2]), to_perm([1,3])]))
    print(mult([to_perm([1,3]), to_perm([1,2])]))
    print(mult([to_perm([]), to_perm([1,2])]))


def test_gens():
    tree = build_tree(1, [to_perm([1,2]), to_perm([1,2,3,4,5])])
    gens = make_gens(tree, [to_perm([1,2]), to_perm([1,2,3,4,5])])

    print(normalize(gens))


def test_chain():
    chain = build_chain([to_perm([2,3,4]), to_perm([3,5])])
    for t in chain.trees:
        print (t.orbit)

    print(chain.calc_size())

    print(build_chain([to_perm([1,2,3,4,5]), to_perm([1,2])]).calc_size())
    print(build_chain([to_perm([1,2,3]), to_perm([4,5])]).calc_size())
    print(build_chain([to_perm([1,2,3,4,5])]).calc_size())
    print(build_chain([to_perm([1,2,3,4]), to_perm([1,3],[2,4]),to_perm([1,4,3,2])]).calc_size())

test_chain()