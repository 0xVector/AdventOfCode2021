def cost(distance):
    return sum(range(1, distance+1))


with open("inputs/day07.txt") as file:
    data = tuple(map(int, file.readline().split(",")))

# Part 1 ===
part1 = min(sum(abs(position-target) for position in data) for target in range(max(data) + 1))


# Part 2 ===
part2 = float("inf")

for target in range(max(data) + 1):
    target_cost = sum(cost(abs(position-target)) for position in data)
    if target_cost < part2:
        part2 = target_cost


print("Part 1:", part1)
print("Part 2:", part2)
