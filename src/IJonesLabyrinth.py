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

# overall time complexity: ~ O((W * H)^2 + W * H)
# overall space complexity: ~ O(W * H)

import os


def read_input_file(file_name: os.PathLike[str]) -> tuple[list[list[str]], int, int]:
    """
    Read the input file and extract matrix dimensions along with the matrix data.

    Args:
    - file_name: Path to the input file.

    Returns:
    - Tuple containing the input matrix, width, and height.
    """
    with open(file_name, "r") as file:
        W, H = map(int, file.readline().split())
        input_matrix = []
        for line in range(H):
            row = list(map(str, file.readline().strip()))  # strip trailing whitespaces,
            # split into characters, and convert to a list
            input_matrix.append(row)
        file.close()
        return input_matrix, W, H


def write_to_output_file(file_name: os.PathLike, path_count: int):
    """
    Write the number of paths to the output file.

    Args:
    - file_name: Path to the output file.
    - path_count: Number of paths to be written to the file.

    Returns:
    - File object.
    """
    with open(file_name, "w") as file:
        file.write(str(path_count))
    file.close()
    return file


def build_chars_positions(
    chars_matrix: list[list],
) -> dict[str: list[tuple[int, int]]]:
    """
    Build a dictionary mapping characters to their positions in the matrix.

    Args:
    - chars_matrix: Input matrix containing characters.

    Returns:
    - Dictionary mapping characters to their positions.
    """
    chars_dict = dict()
    for index_l, line in enumerate(chars_matrix):  # iterate over each row and column
        for index_c, char in enumerate(line):  # of the matrix along with its index
            if char not in chars_dict.keys():
                chars_dict[char] = []
            chars_dict[char].append((index_l, index_c))
    return chars_dict


def build_graph(character_positions: dict[str: [list[tuple[int, int]]]]):
    """
    Build a graph representing connections between character positions.

    Args:
    - character_positions: Dictionary mapping characters to their positions.

    Returns:
    - Graph represented as a dictionary mapping positions to their adjacent positions.
    """
    graph = dict()
    # jumps
    for key, positions in character_positions.items():
        for pos in positions:
            graph[pos] = []
            for i in range(
                len(positions)
            ):  # Check each position for the same character
                if (
                    positions[i][1] > pos[1]
                ):  # if there's a position with greater column index then `jump` to it is possible
                    graph[pos].append(
                        positions[i]
                    )  # and position is added to a list of edges
    # right-only
    for v in graph.keys():
        for key in graph.keys():
            if key not in graph[v]:  # same as if the key is not already connected to v
                # and it's to the right of v then add it to edges for v
                if key[0] == v[0] and key[1] == v[1] + 1:
                    graph[v].append(key)
    return graph


def init_dp(graph, starts):
    """
    Initialize the dynamic programming table.

    Args:
    - graph: Graph represented as a dictionary.
    - starts: List of starting positions.

    Returns:
    - Initialized dynamic programming table.
    """
    dp = {key: 0 for key in graph.keys()}
    for start in starts:
        dp[start] = 1
    return dp


def all_paths(graph: dict[tuple[int, int], list], column_amount, row_amount):
    """
    Find all possible paths in the graph.

    Args:
    - graph: Graph represented as a dictionary.
    - column_amount: Number of columns in the matrix.
    - row_amount: Number of rows in the matrix.

    Returns:
    - Number of possible paths.
    """
    end_points = (
        [(0, column_amount - 1), (row_amount - 1, column_amount - 1)]
        if row_amount > 1
        else [
            (0, column_amount - 1)
        ]  # if input matrix is a single string then there's only one end point
    )
    starts = [(i, 0) for i in range(row_amount)]  # all nodes in first column
    sorted_graph = top_sort(
        graph
    )  # reverse topological sort of given graph to ensure bottom-up dynamic programming approach
    count = 0
    dp = init_dp(graph, starts)
    # Updating the DP table for each vertex in the sorted graph
    for end in end_points:
        for v in sorted_graph:
            for e in graph[v]:
                dp[e] += dp[v]
        count += dp[end]  # Add the count for the current end point to the total count
        dp = init_dp(graph, starts)  # Resetting the DP table for the next end point
    return count


def dfs(graph, vertex, visited, stack):
    """
    Depth-first search traversal.

    Args:
    - graph: Graph represented as a dictionary.
    - vertex: Current vertex.
    - visited: Set of visited vertices.
    - stack: Stack for topological sorting.
    """
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(vertex)


def top_sort(graph: dict[tuple[int, int], list]):
    """
    Perform topological sort on the graph.

    Args:
    - graph: Graph represented as a dictionary.

    Returns:
    - Topologically sorted vertices.
    """
    visited = set()
    stack = []

    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, visited, stack)

    return stack[::-1]


def find_all_possible_paths(input_file, output_file):
    input_matrix, W, H = read_input_file(input_file)
    character_positions = build_chars_positions(input_matrix)
    graph = build_graph(character_positions)
    paths = all_paths(graph, W, H)
    write_to_output_file(output_file, paths)
