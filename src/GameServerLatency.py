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

import heapq


def shortest_paths_to_clients(
    graph: {int: [(int, int)]}, start_point: int, clients: [int]
) -> [int]:
    visited_nodes = set()
    distances_to_vertexes = {key: int(1e10) for key in graph.keys()}
    distances_to_vertexes[start_point] = 0
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (distances_to_vertexes[start_point], start_point))
    while not len(pq) == 0:
        dist_to_vertex, vertex = heapq.heappop(pq)
        if vertex in visited_nodes:
            continue
        visited_nodes.add(vertex)

        for vertex2, latency_v1v2 in graph[vertex]:
            if dist_to_vertex + latency_v1v2 < distances_to_vertexes[vertex2]:
                distances_to_vertexes[vertex2] = dist_to_vertex + latency_v1v2
                heapq.heappush(pq, (distances_to_vertexes[vertex2], vertex2))
    dist_to_clients = []
    for item in range(1, len(distances_to_vertexes) + 1):
        if item in clients:
            dist_to_clients.append(distances_to_vertexes[item])
    return dist_to_clients


def find_server_position(
    v: int, e: int, clients_list: [int], connections: [[int]]
) -> int:
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
        return min(max_routers_latency)
    else:
        return -1
