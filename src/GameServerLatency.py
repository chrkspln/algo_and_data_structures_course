# Рівень 3
# Варіант 1

# Вхiднi данi
# • Перший рядок мiстить N i M — кiлькiсть вузлiв та з’єднань вiдповiдно
# • Другий рядок мiстить перелiк цiлих чисел, роздiлених пробiлом — номери
#   вузлiв, якi є клiєнтами. Усi вузли в мережi нумеруються вiд 1 до N
# • Наступнi M рядкiв мiстять трiйки натуральних чисел startnode, endnode, latency
# — номер початкового вузла, кiнцевого вузла та затримка для кожного з’єднання
#
# Вихiднi данi
# Одне число — мiнiмальне значення найбiльшої затримки до клiєнта
# (яке ми отримаємо при оптимальному розташуваннi сервера).

import os
from src.AVLPriorityQueue import *


def read_input(file_name):
    v, e = 0, 0
    clients_list, connections = [], []
    with open(file_name) as file:
        if os.path.getsize(file_name) != 0:
            v, e = map(int, file.readline().split())
            clients_list = list(map(int, file.readline().split()))
            for _ in range(e):
                start, end, latency = map(int, file.readline().split())
                connections.append([start, end, latency])
    file.close()
    return v, e, clients_list, connections if file else None


def write_output(path, file_name):
    with open(file_name, "w") as file:
        file.write(str(path))
    file.close()
    return file


def shortest_paths_to_clients(
    graph: {int: [(int, int)]}, start_point: int, clients: [int]
) -> [int]:
    visited_nodes = set()
    distances_to_vertexes = {key: int(1e10) for key in graph.keys()}
    distances_to_vertexes[start_point] = 0
    pq = PriorityQueue(start_point, distances_to_vertexes[start_point])

    while not pq.is_empty():
        vertex, dist_to_vertex = pq.dequeue()
        if vertex in visited_nodes:
            continue
        visited_nodes.add(vertex)

        for vertex2, latency_v1v2 in graph[vertex]:
            if dist_to_vertex + latency_v1v2 < distances_to_vertexes[vertex2]:
                distances_to_vertexes[vertex2] = dist_to_vertex + latency_v1v2
                pq.enqueue(vertex2, distances_to_vertexes[vertex2])
    dist_to_clients = []
    for item in range(1, len(distances_to_vertexes) + 1):
        if item in clients:
            dist_to_clients.append(distances_to_vertexes[item])
    return dist_to_clients


def find_server_position(file_name, output_file):
    v, e, clients_list, connections = read_input(file_name)
    if v and e and clients_list and connections:
        routers = set(x for x in range(1, v + 1))
        routers.difference_update(clients_list)
        list_view = {}
        for startnode, endnode, latency in connections:
            if startnode not in list_view.keys():
                list_view[startnode] = []
            if endnode not in list_view.keys():
                list_view[endnode] = []
            list_view[startnode].append((endnode, latency))
            list_view[endnode].append((startnode, latency))
        max_routers_latency = []
        for router in routers:
            max_routers_latency.append(
                max(shortest_paths_to_clients(list_view, router, clients_list))
            )
        latency = min(max_routers_latency)
        return write_output(latency, output_file)
    else:
        return write_output(-1, output_file)
