import heapq
from typing import List, Dict

"""We know how to find the shortest path by Dijkstra, Can we modify it to find the second shortest path"""
"""During our search, we need to consider the red and green light, we can set two states"""


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = self.initialise_graph(edges)
        second_min = self.modified_dijkstra(n, graph, time, change)
        return second_min

    def initialise_graph(self, edges: List[List[int]]) -> Dict[int, List[int]]:
        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])
            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])
        return graph

    def modified_dijkstra(self, n: int, graph: Dict[int, List[int]], time: int, change: int) -> int:
        #shortest distance
        distances = {1: 0}
        #second shortest
        distances_2 = {}
        queue = [(0, 1)]
        visited = [0 for _ in range(n)]
        heapq.heapify(queue)
        while queue:
            dist, node = heapq.heappop(queue)
            visited[node - 1] += 1
            if visited[node - 1] == 2 and node == n:
                return dist
            # if distance is between m*change (m+1)*change we must wait till m+1 change so if odd we wait
            # until m+1 change
            if (dist // change) % 2 == 1:
                # it is red so we wait till the next change
                dist = (dist + change) // change * change
            for neighbor in graph[node]:
                if visited[neighbor - 1] == 2:
                    continue
                if distances.get(neighbor, float('inf')) > dist + time:
                    distances_2[neighbor] = distances.get(neighbor, float('inf'))
                    distances[neighbor] = dist + time
                    heapq.heappush(queue, (dist + time, neighbor))
                elif distances_2.get(neighbor, float('inf')) > dist + time and distances.get(neighbor, float('inf')) != dist + time :
                    distances_2[neighbor] = dist + time
                    heapq.heappush(queue, (dist + time, neighbor))

        return -1


n = 5
edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
time = 3
change = 5
sol = Solution()
print(sol.secondMinimum(n, edges, time, change))
