def sum_calories(calories: str) -> int:
    if not calories:
        return 0

    cleared_list = [int(calorie_str) for calorie_str in calories.split("\n") if calorie_str.strip()]

    return sum(cleared_list)


def sum_each_inventory(elves_inventories: str) -> list[int]:
    calories_by_elves = elves_inventories.replace(" ", "").split("\n\n")
    return list(map(sum_calories, calories_by_elves))


def most_calories(elves_inventories: str) -> int:
    return max(sum_each_inventory(elves_inventories))


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_text = file.read()
        print(most_calories(input_text))
