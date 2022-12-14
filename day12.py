import string
import sys

alphabet = list(string.ascii_lowercase)

with open("input.txt") as f:
    input = f.read().splitlines()
    input = [[n for n in line] for line in input]


def dijkstra(graph, start, target):
    distances = {}
    prev = {}
    Q = set()

    for n in graph:
        distances[n] = sys.maxsize
        prev[n] = None
        Q.add(n)

    distances[start] = 0

    while Q:
        min_dist = sys.maxsize
        u = None

        for n in Q:
            if distances[n] < min_dist:
                min_dist = distances[n]
                u = n

        if u is None:
            u = Q.pop()
        else:
            Q.remove(u)

        if u == target:
            return distances, prev

        xu, yu = u

        candidates = []
        for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            candidates.append((xu + move[0], yu + move[1]))

        candidates = [c for c in candidates if c in Q]

        for c in candidates:
            alt = distances[u]

            xc, yc = c

            if input[yc][xc] == "E":
                current_elevation = alphabet.index("z") + 1
            elif input[yc][xc] == "S":
                current_elevation = 0
            else:
                current_elevation = alphabet.index(input[yc][xc])

            if input[yu][xu] not in ["S", "E"]:
                if current_elevation > alphabet.index(input[yu][xu]) + 1:
                    alt = sys.maxsize
                else:
                    alt += 1

            if alt < distances[c]:
                distances[c] = alt
                prev[c] = u

    return distances, prev


def get_graph_start_target(data):
    graph = set()
    start = None
    target = None

    for y in range(len(data)):
        for x in range(len(data[0])):
            graph.add((x, y))
            if data[y][x] == "S":
                start = (x, y)
            if data[y][x] == "E":
                target = (x, y)

    return graph, start, target


graph, start, target = get_graph_start_target(input)
_, prev = dijkstra(graph, start, target)

path = []
current = target
while True:
    if current == target:
        break
    path.append(current)
    current = prev[current]

print(len(path))


def get_candidates(data):
    candidates = []

    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] in ["a", "S"]:
                candidates.append((x, y))

    return candidates


start_positions = get_candidates(input)
start_positions = [(x, y) for (x, y) in start_positions if x == 0]

lengths = []
for s in start_positions:
    d, p = dijkstra(graph, s, target)

    path = []
    current = target
    last = None
    while True:
        if current == s:
            break

        path.append(current)
        current = p[current]

    lengths.append(len(path))

print(min(lengths))
