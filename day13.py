from itertools import zip_longest

with open("input.txt") as f:
    input = f.read().splitlines()
    input = list(filter(None, input))
    input = [eval(x) for x in input]


def compare(left,right):
    if left is None:
        return -1
    if right is None:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        return 0
     
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right):
            res = compare(l,r)
            if res != 0:
                return res
        return 0
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)


results = []
for i in range(0, len(input), 2):
    left = input[i]
    right = input[i+1]
    results.append(compare(left,right))

indices = [i + 1 for i, x in enumerate(results) if x == -1]
print(sum(indices))

devider_1 = [[2]]
devider_2 = [[6]]

input.append(devider_1)
input.append(devider_2)

for i in range(1, len(input)):
    for k in range(i -1, -1, -1):
        if not (compare(input[k], input[k+1])) == - 1:
            input[k], input[k+1] = input[k+1], input[k]

res = (input.index(devider_1) + 1) * (input.index(devider_2) + 1)
print(res)