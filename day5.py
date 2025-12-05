from utils.read import read_file

def part_one(_input):
    fresh_ingredients_sets = []
    fresh_ingredients_ids = []
    available_ingredients = []
    for line in _input:
        if "-" in line:
            start, end = line.split("-")
            fresh_ingredients_sets.append([start, end])
        else:
            if line != "":
                available_ingredients.append(int(line))

    for ingredient in available_ingredients:
        for _set in fresh_ingredients_sets:
            if ingredient in range(int(_set[0]), int(_set[1]) + 1):
                if ingredient not in fresh_ingredients_ids:
                    fresh_ingredients_ids.append(ingredient)

    print(f"Part 1 - Fresh ingredients that are available: {len(fresh_ingredients_ids)}")


def part_two(_input):
    fresh_ingredients_sets = []
    total_numbers = 0

    for line in _input:
        if "-" in line:
            start, end = line.split("-")
            fresh_ingredients_sets.append([int(start), int(end)])

    fresh_ingredients_sets.sort(key=lambda x: x[0])

    merged = []
    for range_set in fresh_ingredients_sets:
        if not merged or merged[-1][1] + 1 < range_set[0]:
            merged.append(range_set)
        else:
            merged[-1][1] = max(merged[-1][1], range_set[1])

    for range_set in merged:
        total_numbers += range_set[1] - range_set[0] + 1

    print(f"Part 2 - Total numbers in fresh ingredients range: {total_numbers}")

if __name__ == "__main__":
    stringInput = read_file(5, "string", False)
    part_one(stringInput)
    part_two(stringInput)
