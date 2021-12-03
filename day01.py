with open("inputs/day01.txt") as file:
    data = [int(line.strip()) for line in file]

# Part 1 ===
part1, previous = 0, float("inf")

for number in data:
    if number > previous:
        part1 += 1
    previous = number


# Part 2 ===
part2, previous = 0, float("inf")

for i, number in enumerate(data):
    window = sum(data[i:i+3])
    if window > previous:
        part2 += 1
    previous = window


print("Part 1:", part1)
print("Part 2:", part2)
