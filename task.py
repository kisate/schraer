from perm import to_perm, build_perm
from chain import build_chain
from itertools import permutations
from tree import build_tree_for_multi

data1 = {}

for i in range(1, 53):
    if i % 2 == 1:
        data1[i] = (i + 1)//2
    else:
        data1[i] = 26 + i//2

data2 = {}

for i in range(3, 53):
    data2[i] = i - 2

data2[1] = 52
data2[2] = 51

data3 = {}

for i in range(1, 53):
    data3[i] = (i + 25) % 52 + 1

S = [
    build_perm(data1),
    build_perm(data2),
    build_perm(data3)
]


# первая перестановка -- ставит нечетные перед четными
# вторая перестановка -- отправляет первые 2 в конец в обратном порядке
# третья -- меняет половины местами

order = [range(5, 53)]

order.extend([1,2,3,4])

chain = build_chain(S, order)

size_stab_48 = 1
for tree in chain.trees[47:]:
    size_stab_48 *= len(tree.orbit)

#Вероятность, что посетитель получит все тузы, т.е. элементы с 5 по 52 останутся на месте

print(size_stab_48/chain.calc_size())

#Дерево Шраера для [1,2,3,4]

multi_tree = build_tree_for_multi((1,2,3,4), S)


# Чтобы посчитать вероятность того, что будет хотя бы один туз, надо рассмотреть все упорядочивания, 
# где остается хотя бы один туз и для каждого найти размер стабиллизатора для каждого.
# Для этого есть build_tree_for_multi, который находит орбиту какого-то набора элементов. 
# Асимптотика такого метода O(n^9), так как n^4 комбинаций, каждая из которых обрабатывается за n^5,
# поэтому даже писать это смысла нет.
