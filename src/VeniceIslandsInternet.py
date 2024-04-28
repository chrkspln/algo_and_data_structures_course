#   Рівень 2
#   Варіант 1
#
#   До вас звернулась мерія міста Венеції з незвичним проханням.
#   Це місто складається з островів які розділені каналами. Кожен острів має свою унікальну локацію
#   і з`єднаний з іншими островами мостами. Мерія міста хоче провести оптоволоконний інтернет
#   на кожен з островів таким чином, щоб кожен острів був з`єднаний з кожним іншим безпосередньо,
#   або через інші острови. Вам потрібно допомогти порахувати мінімальну довжину кабелів, які потрібно прокласти.
#
#   Вхідні дані:
#   файл islands.csv, який містить матрицю суміжності, де елемент [i][j] вказує на відстань між островами i та j.
#   Вихідні дані:
#   Мінімальна довжина підводних кабелів, які потрібно прокласти.
#   При виборі алгоритму слід вважати, що кількість островів у місті становить N (1 ≤ N ≤ 100)


class DisjointSet:
    def __init__(self, v: int):
        self.rank = [0 for i in range(v + 1)]
        self.parent = [v for v in range(v + 2)]

    def find_main_parent(self, item: int):
        if self.parent[item] == item:
            return item
        return self.parent[item] == self.find_main_parent(self.parent[item])

    def rank_union(self, item1: int, item2: int):
        main_parent1 = self.find_main_parent(item1)
        main_parent2 = self.find_main_parent(item2)
        if main_parent1 == main_parent2:
            return

        if self.rank[main_parent1] > self.rank[main_parent2]:
            self.parent[main_parent2] = main_parent1

        elif self.rank[main_parent1] < self.rank[main_parent2]:
            self.parent[main_parent1] = main_parent2

        else:
            self.parent[main_parent1] = main_parent2
            self.rank[main_parent2] += 1


def min_span_tree(v: int, adj_dict: dict[int, list[tuple[int, int]]]):
    dsj_set = DisjointSet(v)
    min_weight = 0
    for i in adj_dict.items():
        vertex1 = i[0]
        for l in range(len(adj_dict[vertex1])):
            vertex2, weight = adj_dict[vertex1][l]
            if dsj_set.find_main_parent(vertex1) != dsj_set.find_main_parent(vertex2):
                min_weight += weight
                dsj_set.rank_union(vertex1, vertex2)
    return min_weight


def matrix_to_dict(input_matrix):
    adj_dict = dict()

    if len(input_matrix) != 0:
        for i in range(len(input_matrix)):
            for j in range(len(input_matrix[0])):
                if input_matrix[i][j] != 0 and i != 0 and j != 0:
                    if i not in adj_dict.keys():
                        adj_dict[i] = []
                    adj_dict[i].append((j, input_matrix[i][j]))

        return sorted(
            adj_dict.items(), key=lambda item: sorted(item[1], key=lambda x: x[1])
        )
    else:
        return []


def read_input_file(file_name):
    input_matrix = []
    with open(file_name, "r") as file:
        for line in file:
            row = list(map(int, line.split(",")))
            input_matrix.append(row)
    file.close()
    return input_matrix


def write_to_output_file(file_name, min_cable_length):
    with open(file_name, "w") as file:
        file.write(str(min_cable_length))
    file.close()
    return file


def find_min_cable_length(input_file_name, output_file_name):
    input_matrix = read_input_file(input_file_name)
    adjacency_dict = dict(matrix_to_dict(input_matrix))
    if len(adjacency_dict) != 0:
        min_cable_length = min_span_tree(len(adjacency_dict.keys()), adjacency_dict)
    else:
        min_cable_length = ""
    return write_to_output_file(output_file_name, min_cable_length)
