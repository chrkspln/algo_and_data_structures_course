#   Рівень 3
#   Варіант 1
#   Створити функцію на мові програмування Python, яка приймає дві стрічки: "haystack" (довільний текст)
#   та "needle" (шукана стрічка). Програма повинна знайти індекси всіх входжень стрічки "needle"
#   в стрічці "haystack" та повернути цей індекс, використовуючи
#   метод скінченних автоматів для пошуку підстрічки у стрічці


def next_state(pattern, state, c):
    if state < len(pattern) and c == pattern[state]:
        return state + 1

    pattern += c
    for i in range(state, 0, -1):
        prefix = pattern[0:i]
        suffix = pattern[-i:]
        if prefix == suffix:
            return i
    return 0


def transition_table(pattern, alphabet):
    table = [[0 for i in range(len(alphabet))] for _ in range(len(pattern) + 1)]
    for state in range(len(pattern) + 1):
        for c in alphabet:
            table[state][alphabet.index(c)] = next_state(pattern, state, c)
    return table


def finite_automata_search(pattern, haystack):
    if pattern and haystack and len(pattern) <= len(haystack):
        alphabet = list(sorted(set(haystack)))
        indices = []
        table = transition_table(pattern, alphabet)
        state = 0
        for i in range(len(haystack)):
            state = table[state][alphabet.index(haystack[i])]
            if state == len(pattern):
                indices.append(i - len(pattern) + 1)
        return indices
    else:
        return []
