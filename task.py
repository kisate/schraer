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

# Посчитаем куда может перейти 1, 2, 3, 4

multi_tree = build_tree_for_multi((1,2,3,4), S)

# Посчитаем цепь

chain = build_chain(S)

size_stab_4 = 1
for tree in chain.trees[:4]:
    size_stab_4 *= len(tree.orbit)

# Найдем размер стабиллизатора 1, 2, 3, 4 

size_stab_4 = chain.calc_size() // size_stab_4

# То, что получает посетитель, -- какая-то перестановка из полученной группы.
# Чтобы посетитель получил все тузы, эта перестановка должна переводить 1, 2, 3, 4 в само себя.
# Тогда, чтобы посчитать вероятность, что будут все тузы, найдем все варианты,
# при которых 1, 2, 3, 4 переходит в себя, умножим их число на размер стабилизатора и поделим на размер группы.
# Так как все перестановки, которые переводят 1,2,3,4 в какой-то конкретный порядок, отличаются на элемент стабилизатора,
# то мы как раз получим нужную вероятность.
# Для хотя бы одного то же самое сделаем. 

amount1 = 0
amount2 = 0
for x in multi_tree:
    if 1 in x and 2 in x and 3 in x and 4 in x:
        amount1 += 1
    if 1 in x or 2 in x or 3 in x or 4 in x:
        amount2 += 1

# Вероятность, что будут все тузы
print(amount1*size_stab_4/chain.calc_size())


# Вероятность, что будет хотя бы один
print(amount2*size_stab_4/chain.calc_size())