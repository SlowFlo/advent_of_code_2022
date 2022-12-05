def most_calories(input: str):
    if not input:
        return 0

    cleared_list = [int(calorie_str) for calorie_str in input.split("\n") if calorie_str.strip()]

    return sum(cleared_list)
