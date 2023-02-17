import re

with open("input.txt") as f:
    input = f.read().splitlines()

sensors = []
beacons = set()
distances = {}

for row in input:
    sx, sy, bx, by = re.findall(r"-?\d+", row)
    sx, sy, bx, by = int(sx), int(sy), int(bx), int(by)
    sensors.append((sx, sy))
    beacons.add((bx, by))

    distances[(sx, sy)] = abs(sx - bx) + abs(sy - by)

y = 2000000

min_x = min([x for (x, _) in sensors] + [x for (x, _) in beacons])
max_x = max([x for (x, _) in sensors] + [x for (x, _) in beacons])

cands = [(x, y) for x in range(min_x, max_x + 1)]
count = 0
for cand in cands:
    for s in sensors:
        d = abs(cand[0] - s[0]) + abs(cand[1] - s[1])
        if d <= distances[s] and (cand not in beacons):
            count += 1
            break

print(count)
