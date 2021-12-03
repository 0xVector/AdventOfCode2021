def count_ones_at(index, numbers):
    return sum(1 if num[index] == '1' else 0 for num in numbers)


def remove_all_with(bit, index, numbers):
    numbers -= {num if num[index] == bit else None for num in numbers}


def search_for_rating(oxygen_mode):  # False for CO2 mode
    candidates = set(data)   # Get a copy of data
    a, b = ("0", "1") if oxygen_mode else ("1", "0")

    for i in range(len(data[0])):
        if count_ones_at(i, candidates) >= len(candidates) / 2:  # 1s more common
            remove_all_with(a, i, candidates)  # In oxygen mode, removing 0s
        else:  # 0s more common
            remove_all_with(b, i, candidates)  # In oxygen mode, removing 1s

        if len(candidates) == 1:
            return int(candidates.pop(), 2)


with open("inputs/day03.txt") as file:
    data = [line.strip() for line in file]

# Part 1 ===
gamma, epsilon = "", ""

for i in range(len(data[0])):
    if count_ones_at(i, data) > len(data)/2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

part1 = int("".join(gamma), 2) * int("".join(epsilon), 2)


# Part 2 ===
oxygen, co2 = search_for_rating(True), search_for_rating(False)
part2 = oxygen * co2


print("Part 1:", part1)
print("Part 2:", part2)
