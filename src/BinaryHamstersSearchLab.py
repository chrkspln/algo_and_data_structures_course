import unittest


def how_many_hamsters(hamsters_list, hamsters_quantity, daily_food):
    # якщо список пустий - повертаємо 0
    if not hamsters_list:
        return 0

    result = hamsters_search(hamsters_list, len(hamsters_list) - 1, daily_food, 0, 0)
    return result


def hamsters_search(list, end, food_av, count, prev_count):
    start = 0
    mid = (start + end) // 2
    food_needed_list = []

    for for_one, greedy in list:
        food_needed_list.append(for_one + greedy * mid)

    food_needed_list = sorted(food_needed_list)
    required_food = sum(food_needed_list[:mid])

    if required_food > food_av:
        if prev_count == count:
            return mid + 1
        elif prev_count < count:
            prev_count = count
            hamsters_search(list[:mid], mid - 1, food_av, 0, prev_count)
            return mid + 1
    elif required_food < food_av and len(list) != 1:
        if prev_count > count:
            return mid + 1
        elif prev_count == count:
            count += 1
            hamsters_search(list[mid:], len(list) - 1, food_av, count, prev_count)
            return mid + 1
    else:
        return len(food_needed_list)
