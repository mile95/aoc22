from collections import defaultdict

with open("input.txt") as f:
    input = f.read().splitlines()


filepath = []
sizes = defaultdict(int)
for ins in input:
    if "$ cd" in ins:
        d = ins.split()[-1]
        if d == "..":
            filepath.pop()
        else:
            filepath.append(d)
    elif "$ ls " in ins:
        continue
    else:
        size, _ = ins.split()
        if size.isdigit():
            size = int(size)
            for i in range(len(filepath)):
                sizes["/".join(filepath[: i + 1])] += size

s = 0
for k, v in sizes.items():
    if v <= 100000:
        s += v
print(s)

candidates = []
needed = 30000000 - (70000000 - sizes["/"])
for k, v in sizes.items():
    if v > needed:
        candidates.append(v)

print(min(candidates))
