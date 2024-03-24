# Рівень 3
# Варіант 4

# Прямокутне поле має форму матриці M × N, потрібно знайти найкоротший шлях від
# будь-якої клітинки в першому стовпці до будь-якої клітинки в останньому стовпці матриці.
# Датчики позначаються в матриці значенням 0, і всі її вісім суміжних осередків також
# можуть активувати датчики. Шлях можна побудувати лише з комірок зі значенням 1,
# і в будь-який момент ми можемо рухатися лише на один крок в одному з чотирьох напрямків.
# Допустимі ходи:
#
# Вгору:    (x, y) -> (x, y + 1)
# Ліворуч:  (x, y) -> (x - 1, y)
# Вниз:     (x, y) -> (x, y - 1)
# Праворуч: (x, y) -> (x + 1, y)
# Алгоритм має вивести довжину найкоротшого шляху, або -1 якщо такого не існує.


def get_start_nodes_list(grid: [[int]]) -> [(int, int)]:
    row = 0
    start_nodes = []
    while row < len(grid) - 1:
        if grid[row][0] == 1:
            start_nodes.append((row, 0))
        row += 1
    return start_nodes


def set_0(grid: [[int]]) -> [[int]]:
    mines_positions = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                mines_positions.append([y, x])
    for position in mines_positions:
        position_neighbors = get_neighbors(position, grid)
        for y, x in position_neighbors:
            grid[y][x] = 0
    return grid


def get_neighbors(node: (int, int), grid: [[int]]) -> list:
    y = node[0]
    x = node[1]
    neighboring_nodes = []
    # moving right
    if x < len(grid[0]) - 1:
        if grid[y][x + 1] == 1:
            neighboring_nodes.append((y, x + 1))
    # moving left
    if x > 0:
        if grid[y][x - 1] == 1:
            neighboring_nodes.append((y, x - 1))
    # moving down
    if y < len(grid) - 1:
        if grid[y + 1][x] == 1:
            neighboring_nodes.append((y + 1, x))
    # moving up
    if y > 0:
        if grid[y - 1][x] == 1:
            neighboring_nodes.append((y - 1, x))
    # taking diagonal nodes if were zeroing the grig
    if grid[y][x] == 0:
        if x > 0 and y > 0:
            neighboring_nodes.append((y - 1, x - 1))
        if x > 0 and y < len(grid) - 1:
            neighboring_nodes.append((y + 1, x - 1))
        if (x < len(grid[0]) - 1) and y > 0:
            neighboring_nodes.append((y - 1, x + 1))
        if (x < len(grid[0]) - 1) and y < len(grid) - 1:
            neighboring_nodes.append((y + 1, x + 1))

    return neighboring_nodes


def find_path(start_nodes: [(int, int)], grid: [[int]]):
    shortest_path_list = []
    for start_point in start_nodes:
        visited = []
        queue = [(start_point, [])]
        while queue:
            node, path = queue.pop(0)
            path.append(node)
            visited.append(node)

            if node[1] == len(grid[0]) - 1:
                shortest_path_list.append(len(path))

            neighboring_nodes = get_neighbors(node, grid)
            for neighbor in neighboring_nodes:
                if neighbor not in visited:
                    queue.append((neighbor, path[:]))

    return min(shortest_path_list) if shortest_path_list else -1


def short_mines_path_search(grid: [[int]]) -> int:
    grid = set_0(grid)
    start_nodes = get_start_nodes_list(grid)
    return find_path(start_nodes, grid)
