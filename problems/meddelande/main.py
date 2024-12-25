grid = []
rows, columns = tuple(input().split())

for i in range(0, int(rows)):
    grid.append(list(input()))


def walk():
    for x in range(0, int(rows)):
        for y in range(0, int(columns)):
            if grid[x][y] == ".":
                continue
            yield grid[x][y]


print(''.join(walk()))
