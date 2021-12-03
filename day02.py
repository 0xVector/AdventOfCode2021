with open("inputs/day02.txt") as file:
    data = tuple(line.split() for line in file.readlines())

# Part 1 ===
x, y = 0, 0

for line in data:
    instruction, value = line[0], int(line[1])
    if instruction == "forward":
        x += value
    elif instruction == "up":
        y -= value
    elif instruction == "down":
        y += value

part1 = x * y


# Part 2 ===
x, y, aim = 0, 0, 0

for line in data:
    instruction, value = line[0], int(line[1])
    if instruction == "forward":
        x += value
        y += aim * value
    elif instruction == "up":
        aim -= value
    elif instruction == "down":
        aim += value

part2 = x * y


print("Part 1:", part1)
print("Part 2:", part2)
