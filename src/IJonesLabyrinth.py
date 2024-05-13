#   В пошуках Святого Грааля Iндiана Джонс зiткнувся з небезпечним випробуванням.
#   Йому потрiбно пройти крiзь прямокутний коридор, який складається з крихких плит.
#   Для заданого коридору, пiдрахуйте, скiльки всього iснує способiв пройти його успiшно.
#   Вхiднi данi
#   Вхiдний файл ijones .in складається з H + 1 рядкiв.
#   • Перший рядок мiстить два числа W i H, роздiленi пробiлом: W — ширина
#   коридору, H — висота коридору, 1 <= W, H <= 2000.
#   • Кожен з наступних H рядкiв мiстить слово довжиною W символiв, яке складається
#   з малих латинських лiтер вiд a до z.
#   Вихiднi данi
#   Вихiдний файл ijones .out повинен мiстити одне цiле число — кiлькiсть рiзних
#   шляхiв для виходу з коридору.


import os
from typing import TextIO


def read_input_file(file_name: os.PathLike[str]) -> list[list]:
    with open(file_name, "r") as file:
        W, H = map(int, file.readline().split())
        input_matrix = [[] * W] * H
        for line in range(H):
            input_matrix.append(file.read())  # ?
            row = list(map(str, file.readline()))
            # TODO: appending chars seems wrong here, redo
            input_matrix.append(row)
        file.close()
        return input_matrix, W, H


def write_to_output_file(file_name: os.PathLike, pathways_count: int) -> TextIO:
    with open(file_name, "w") as file:
        file.write(str(pathways_count))
    file.close()
    return file


"""
reviewed, works as intended when i added enumerate()
"""


def build_chars_positions(
        chars_matrix: list[list],
) -> dict[str: list[tuple[int, int]]]:
    chars_dict = dict()
    for index_l, line in enumerate(chars_matrix):
        for index_c, char in enumerate(line):
            if char not in chars_dict.keys():
                chars_dict[char] = []
            chars_dict[char].append((index_l, index_c))
    return chars_dict


"""
reviewed, works as intended
"""


def build_graph(character_positions: dict[str: [list[tuple[int, int]]]]):
    graph = dict()
    # jumps
    for key, positions in character_positions.items():
        for pos in positions:
            graph[pos] = []
            for i in range(len(positions)):
                if positions[i][1] < pos[1]:
                    graph[pos].append(positions[i])
    # left-only
    for v in graph.keys():
        for key in graph.keys():
            if key not in graph[v]:
                if key[0] == v[0] and key[1] == v[1] - 1:
                    graph[v].append(key)
    return graph


# TODO: make pathfinding w/o recursion and make it work on 1d array
def all_paths(graph: dict[tuple[int, int], list], last_row, last_column):
    end_points = [(0, last_column), (last_row, last_column)]
    starts = [(i, 0) for i in range(last_row + 1)]
    paths = 0
    for i in end_points:
        paths += counting(graph, i, starts)
    return paths


def counting(graph, start, ends, count=0):
    if start in ends:
        return 1
    for v in graph[start]:
        count += counting(graph, v, ends)
    return count
