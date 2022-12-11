with open("input.txt") as f:
    input = f.read().splitlines()

x = 1
c = 0
s = 0
last_injected = 0

for ins in input:
    if c in [20, 60, 100, 140, 180, 220] and c != last_injected:
        s += x * c
        last_injected = c
    if ins == "noop":
        c += 1
    if "addx" in ins:
        val = int(ins.split()[1])
        for i in range(2):
            c += 1
            if c in [20, 60, 100, 140, 180, 220] and c != last_injected:
                last_injected = c
                s += x * c
            if i == 1:
                x += val
print(s)


x = 1
c = 0
last_injected = 0
crts = [""] * 6

for ins in input:
    if ins == "noop":
        if (c - 40 * (c // 40)) in range(x - 1, x + 2):
            crts[c // 40] += "#"
        else:
            crts[c // 40] += "."

        c += 1
    if "addx" in ins:
        val = int(ins.split()[1])
        for i in range(2):
            if (c - 40 * (c // 40)) in range(x - 1, x + 2):
                crts[c // 40] += "#"
            else:
                crts[c // 40] += "."
            c += 1
            if i == 1:
                x += val


for crt in crts:
    print(crt)
