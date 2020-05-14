

line = input()

while line != 'exit':
    cycles = []
    while line != '':
        cycles.append(Cycle([int(x) for x in line.split()]))
        line = input()
    for r in mult(cycles):
        print(r)
    line = input()