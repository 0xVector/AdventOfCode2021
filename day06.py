def simulate(days):
    fish_by_age = {age: data.count(age) for age in range(9)}
    new_fish = 0

    for day in range(days):
        for age, fish in fish_by_age.items():
            if age == 0:
                new_fish = fish_by_age[0]
            else:
                fish_by_age[age-1] = fish

        fish_by_age[6] += new_fish
        fish_by_age[8] = new_fish

    return sum(fish_by_age.values())


with open("inputs/day06.txt") as file:
    data = list(map(int, file.readline().split(",")))

# Part 1 ===
part1 = simulate(80)


# Part 2 ===
part2 = simulate(256)


print("Part 1:", part1)
print("Part 2:", part2)
