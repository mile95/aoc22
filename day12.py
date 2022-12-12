import string

alphabet = list(string.ascii_lowercase)

with open("input.txt") as f:
    input = f.read().splitlines()


def find_start():
    for i, r in enumerate(input):
        if 'S' in r:
            return (i, r.index('S'))

def solve(pos, path):
    x, y = pos
    val = input[x][y]
    candidates = []
    for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        xc, yc = move
        try:
            cand = input[x + xc][y + yc]
            current_height = 0 if val == "S" else alphabet.index(val)
            if (x + xc, y + yc) not in path:
                cand_height = alphabet.index('z') if cand == "E" else alphabet.index(cand)
                if (
                    (cand_height <= (current_height + 1))
                    and (x + xc >= 0 and y + yc >= 0)
                ):
                    candidates.append((x + xc, y + yc))
        except IndexError:
            pass
    for c in candidates:
        if input[c[0]][c[1]] == 'E':
            print("Woho! Found E!")
            print(len(path))
            break
        else:
            path.append(pos)
            solve(c, path)

start_pos = find_start()
solve(start_pos, [])
