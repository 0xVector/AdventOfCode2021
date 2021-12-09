import grids


def overlaps():
    count = 0
    for tile in grid:
        if tile.data > 1:
            count += 1
    return count


with open("inputs/day05.txt") as file:
    data = []
    for line in file:
        coord1, coord2 = line.split(" -> ")
        data.append((tuple(map(int, coord1.split(","))), tuple(map(int, coord2.split(",")))))

# Part 1 ===
grid = grids.Grid(width=1000, height=1000, fill=0)
for coord1, coord2 in data:
    x1, y1 = coord1
    x2, y2 = coord2

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] += 1

    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] += 1

part1 = overlaps()
print(grid)
print()


# Part 2 ===
for coord1, coord2 in data:
    x1, y1 = coord1
    x2, y2 = coord2

    if x1 == x2 or y1 == y2:
        continue

    range_x = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
    range_y = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
    for x, y in zip(range_x, range_y):
        grid[y][x] += 1
        # nemozu byt obe v asc poradi treba to robit v danom

part2 = overlaps()
print(grid)


print("Part 1:", part1)
print("Part 2:", part2)
