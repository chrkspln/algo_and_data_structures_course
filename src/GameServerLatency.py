# Рівень 3
# Варіант 1
import queue


def shortest_paths_to_clients(graph: {int: [(int, int)]}, start_point: int) -> [int]:
    visited_nodes = set()
    distances_to_vertexes = {key: int(1e10) for key in graph.keys()}
    distances_to_vertexes[start_point] = 0
    pq = queue.PriorityQueue()
    pq.put((start_point, distances_to_vertexes[start_point]))
    while pq:
        vertex, dist_to_vertex = pq.get()
        if vertex in visited_nodes:
            continue
        visited_nodes.add(vertex)

        for edges in graph[vertex]:
            for edge_num in range(len(edges)):
                vertex2, latency_v1v2 = edges[edge_num]
                """
                TypeError: cannot unpack non-iterable int object
                """
                if dist_to_vertex + latency_v1v2 < distances_to_vertexes[vertex2]:
                    distances_to_vertexes[vertex2] = dist_to_vertex + latency_v1v2
                    pq.put(vertex2, distances_to_vertexes[vertex2])
    return distances_to_vertexes


def find_server_position(
    v: int, e: int, clients_list: [int], connections: [[int]]
) -> int:
    if v and e and clients_list and connections:
        routers = set(x for x in range(1, v + 1))
        routers.difference(clients_list)
        list_view = {}
        for startnode, endnode, latency in connections:
            if startnode not in list_view.keys():
                list_view[startnode] = []
            if endnode not in list_view.keys():
                list_view[endnode] = []
            list_view[startnode].append((endnode, latency))
            list_view[endnode].append((startnode, latency))
        max_latency = 0
        for router in routers:
            max_latency = max(shortest_paths_to_clients(list_view, router), max_latency)
        return max_latency
    else:
        return -1
