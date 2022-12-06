import re


def sum_calories(calories: str) -> int:
    if not calories:
        return 0

    cleared_list = [int(calorie_str) for calorie_str in calories.split("\n") if calorie_str.strip()]

    return sum(cleared_list)


def most_calories(input: str):

    elves_regex = re.compile(r"\n\s*\n")
    calories_by_elves = elves_regex.split(input)

    return max(map(sum_calories, calories_by_elves))
