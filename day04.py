def get_hit(num, board):
    for y, row in enumerate(board):
        if num in row:
            return y, row.index(num)
    return None


def check(grid_i):
    board = hits[grid_i]
    for row in board:
        if all(row):
            return True
    for x in range(len(board[0])):
        if all(board[y][x] for y in range(len(board))):
            return True
    return False


def get_score(board, board_i, latest_number):
    x=sum(board[i][j] if not hits[board_i][i][j] else 0 for i in range(5) for j in range(5))
    return x * latest_number


with open("inputs/day04.txt") as file:
    numbers = tuple(map(int, file.readline().split(",")))
    file.readline()  # first empty line

    grids, grid = [], []
    for line in map(lambda x: x.strip(), file.readlines()):
        if line:
            grid.append(tuple(map(int, line.split())))
            if len(grid) == 5:
                grids.append(grid)
                grid = []

# Part 1 & 2 ===
part1, part2 = None, None
won_count = 0
grids_won = [None] * len(grids)
hits = tuple(tuple([False]*5 for i in range(5)) for j in range(len(grids)))

for number in numbers:
    for i, grid in enumerate(grids):
        if grids_won[i]:
            continue

        if hit := get_hit(number, grid):
            row, column = hit
            hits[i][row][column] = True
        if check(i):
            grids_won[i] = True
            won_count += 1
            if not part1:
                part1 = get_score(grid, i, number)
            if won_count == len(grids):  # Last winning
                part2 = get_score(grid, i, number)
                break


print("Part 1:", part1)
print("Part 2:", part2)
