def how_many_hamsters(hamsters_list, hamsters_quantity, daily_food):
    # якщо список пустий - повертаємо 0
    if not hamsters_list:
        return 0
    count = [0] * hamsters_quantity
    return hamsters_search(hamsters_list, 0, len(hamsters_list) - 1, count, daily_food)


def hamsters_search(list, start, end, count, food_available):
    mid = (start + end) // 2
    temp_array = sorted([x[0] + x[1] * mid for x in list])
    if sum(temp_array[:mid + 1]) == food_available:
        return mid + 1
    elif sum(temp_array[:mid + 1]) > food_available:
        count[mid] = sum(temp_array[:mid + 1])
        return hamsters_search(list, start, mid - 1, count, food_available)
    else:
        if mid + 1 > len(count) - 1:
            return mid + 1
        count[mid] = sum(temp_array[:mid + 1])
        if count[mid + 1] > food_available:
            return mid + 1
        else:
            return hamsters_search(list, mid + 1, end, count, food_available)

