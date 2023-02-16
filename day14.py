from collections import defaultdict

with open("input.txt") as f:
    input = f.read().splitlines()

rocks = defaultdict(set)

for path in input:
    steps = path.split(" -> ")
    prev = None
    for step in steps:
        col = int(step.split(",")[0])
        row = int(step.split(",")[1])
        if not prev:
            rocks[col].add(row)
        else:
            col_diff = int(step.split(",")[0]) - prev[0]
            row_diff = int(step.split(",")[1]) - prev[1]

            if col_diff == 0 and row_diff > 0:
                for x in range(prev[1] + 1, prev[1] + row_diff + 1):
                    rocks[col].add(x)
            elif col_diff == 0 and row_diff < 0:
                for x in range(prev[1], row - 1, -1):
                    rocks[col].add(x)
            elif row_diff == 0 and col_diff > 0:
                for x in range(prev[0] + 1, prev[0] + col_diff + 1):
                    rocks[x].add(row)
            elif row_diff == 0 and col_diff < 0:
                for x in range(prev[0], col - 1, -1):
                    rocks[x].add(row)

        prev = (col, row)

max_level = 0
for rock in rocks:
    max_level = max(max_level, max(rocks[rock]))

sand = []
start = (500, 0)
cp = start

while True:
    # down, dig left, dig right
    candidates = [(cp[0], cp[1] + 1), (cp[0] - 1, cp[1] + 1), (cp[0] + 1, cp[1] + 1)]
    moved = False
    if cp[1] > max_level:
        break

    for i, cand in enumerate(candidates):
        if (cand not in sand) and (cand[1] not in rocks[cand[0]]):
            cp = cand
            moved = True
            break
        elif i == (len(candidates) - 1):
            sand.append(cp)
            break
    if not moved:
        cp = start

print("Part A: " + str(len(sand)))

sand = []
start = (500, 0)
cp = start


max_level = 0
for rock in rocks:
    max_level = max(max_level, max(rocks[rock]))


while True:
    # down, dig left, dig right
    candidates = [(cp[0], cp[1] + 1), (cp[0] - 1, cp[1] + 1), (cp[0] + 1, cp[1] + 1)]
    moved = False

    for i, cand in enumerate(candidates):
        if (cand not in sand) and (
            cand[1] not in rocks[cand[0]] and (cand[1] < (max_level + 2))
        ):
            cp = cand
            moved = True
            break
        elif i == (len(candidates) - 1):
            sand.append(cp)
            break
    if not moved:
        if cp == start:
            break
        cp = start

print("Part B: " + str(len(sand)))
