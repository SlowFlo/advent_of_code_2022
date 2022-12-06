def sum_calories(calories: str) -> int:
    if not calories:
        return 0

    cleared_list = [int(calorie_str) for calorie_str in calories.split("\n") if calorie_str.strip()]

    return sum(cleared_list)


def most_calories(elves_inventories: str) -> int:
    calories_by_elves = elves_inventories.replace(" ", "").split("\n\n")

    return max(map(sum_calories, calories_by_elves))


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_text = file.read()
        print(most_calories(input_text))
