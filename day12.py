import string

alphabet = list(string.ascii_lowercase)

with open("input.txt") as f:
    input = f.read().splitlines()


def find_index(item):
    for i, r in enumerate(input):
        if item in r:
            return (i, r.index(item))


def dijkstra(graph, start_pos, target):
    distances = {}
    prev = {}
    Q = set()

    for n in graph:
        distances[n] = 100000000
        prev[n] = None
        Q.add(n)

    distances[start_pos] = 0

    while len(Q) > 0:
        min_dist = 100000000
        u = None

        for n in Q:
            if distances[n] < min_dist:
                min_dist = distances[n]
                u = n

        if u is None:
            u = Q.pop()
        else:
            Q.remove(u)

        xu, yu = u
        val = input[xu][yu]

        if u == target:
            return distances, prev

        candidates = []
        for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            candidates.append((xu + move[0], yu + move[1]))

        # Compute cost as the height.
        for c in candidates:
            alt = distances[u]
            try:
                c_val = input[c[0]][c[1]]

                if c_val == "E":
                    c_h = alphabet.index("z")
                elif c_val == "S":
                    c_h = 0
                else:
                    c_h = alphabet.index(c_val)

                if val not in ["E", "S"]:
                    if c_h > alphabet.index(val) + 1:
                        alt = 100000000
                    else:
                        alt += 1
                if alt < distances[c]:
                    distances[c] = alt
                    prev[c] = u
            # Lazy way of handling boundaries in the grid!
            except Exception:
                pass

    return distances, prev


start_pos = find_index("S")
end_pos = find_index("E")

graph = []
for x in range(len(input)):
    for y in range(len(input[0])):
        graph.append((x, y))

distances, prev = dijkstra(graph, start_pos, "E")

path = []
while True:
    if end_pos == start_pos:
        break
    path.append(end_pos)
    end_pos = prev[end_pos]

print(len(path))
