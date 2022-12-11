with open("input.txt") as f:
    input = f.read().splitlines()
    moves = []
    for l in input:
        d, q = l.split()
        moves.append((d, int(q)))


dir = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def follow(h, t):
    x, y = h[0] - t[0], h[1] - t[1]
    if abs(x) > 1 or abs(y) > 1:
        return (
            t[0] + (0 if x == 0 else x // abs(x)),
            t[1] + (0 if y == 0 else y // abs(y)),
        )
    return t


def solve(knots):
    ropes = [(0, 0)] * knots
    visited = {ropes[-1]}
    for move in moves:
        change = dir[move[0]]
        for _ in range(move[1]):
            head = ropes[0]
            ropes[0] = head[0] + change[0], head[1] + change[1]
            for x in range(1, knots):
                ropes[x] = follow(ropes[x - 1], ropes[x])
            visited.add(ropes[-1])
    return len(visited)


print(solve(2))
print(solve(10))
