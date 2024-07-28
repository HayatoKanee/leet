import heapq
from collections import deque
from typing import List, Dict, Tuple

"""Improvement on speed, we create all pair shortest path"""


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = self.initialize_graph(original, changed, cost)
        n = len(source)
        distances = {}
        cost = 0
        for i in range(n):
            if source[i] not in distances:
                distances[source[i]] = self.dijkstra(source[i], graph)
            if source[i] == target[i]:
                continue
            current_cost = distances[source[i]].get(target[i], -1)
            if current_cost == -1:
                return current_cost
            cost += current_cost
        return cost

    def initialize_graph(self, original: List[str], changed: List[str], cost: List[int]) -> Dict[str, List[
        Tuple[str, int]]]:
        n = len(original)
        graph = {}
        for i in range(n):
            adjacent_nodes = graph.get(original[i])
            if adjacent_nodes:
                adjacent_nodes.append((changed[i], cost[i]))
            else:
                graph[original[i]] = [(changed[i], cost[i])]
        return graph

    def dijkstra(self, source: str, graph: Dict[str, List[Tuple[str, int]]]):
        distance = {source: 0}
        queue = [(0, source)]
        heapq.heapify(queue)
        while queue:
            current = heapq.heappop(queue)
            if not graph.get(current[1]):
                continue
            for neighbor in graph[current[1]]:
                w = current[0] + neighbor[1]
                if distance.get(neighbor[0], float('inf')) > w:
                    distance[neighbor[0]] = w
                    heapq.heappush(queue, (w, neighbor[0]))
        return distance


solution = Solution()
source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]
print(solution.minimumCost(source, target, original, changed, cost))
