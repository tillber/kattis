# https://open.kattis.com/problems/meddelande

grid = []
rows, columns = map(int, (input().split()))

for i in range(int(rows)):
    grid.append(list(input()))


for x in range(int(rows)):
    for y in range(int(columns)):
        if grid[x][y] == ".":
            continue
        print(grid[x][y], end="")
