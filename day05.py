with open("input.txt") as f:
    input = f.read().splitlines()


moves = [x for x in input if "move" in x]
setup = [x for x in input if "[" in x]

setup = [*zip(*setup)]

init = []
for s in setup:
    filtered = "".join(filter(str.isalpha, s))
    if filtered:
        init.append(filtered[::-1])

for move in moves:
    q = int(move.split()[1])
    f = int(move.split()[3])
    t = int(move.split()[5])

    to_move = init[f - 1][-q:]

    # for part A, iteratate the reversed list. to_move[::-1]
    for m in to_move:
        init[t - 1] += m

    init[f - 1] = init[f - 1][:-q]

word = ""

for i in init:
    word += i[-1]

print(word)
