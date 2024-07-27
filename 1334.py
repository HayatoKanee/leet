import heapq
from typing import List


class Node:
    def __init__(self, index, parent, distance):
        self.index = index
        self.distance = distance
        self.parent = parent

    def __lt__(self, other):
        return self.distance < other.distance


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        queues, adjacent_lists = self.initialise(n, edges, distanceThreshold)
        for i in range(n):
            self.dijkstra(n, edges, i, queues, distanceThreshold, adjacent_lists)

    def initialise(self, n: int, edges: List[List[int]], distanceThreshold: int):
        """We loop through the edges once to build our initial queues"""
        queues = []
        adjacent_lists = []
        for i in range(n):
            queue = []
            for j in range(n):
                if i == j:
                    heapq.heappush(queue,
                               Node(j, -1, 0))
                else:
                    heapq.heappush(queue, Node(j, -1, distanceThreshold + 1))

                queues.append(queue)
                adjacent_lists.append([])

                for edge in edges:
                # edge is [startnode, endnode, weight]
                    startnode = edge[0]
                endnode = edge[1]
                weight = edge[2]
                queues[startnode][endnode] = (-1, weight)
                adjacent_lists[startnode].append(endnode)
        return queues, adjacent_lists

    def dijkstra(self, n: int, edges: List[List[int]], source: int, queues, distanceThreshold: int, adjacent_lists):
        mins = []
        for i in range(n):
            mins.append(-1, -1)
        """if node 0 is the source, initital queue would be 
        [(0,-1,0),(1,-1, 2),(2,-1, inf), (3,-1, inf), (4,-1, 8)]"""
        queue = queues[source]
        while queue:
            node = heapq.heappop(queue)
            for adj_node in adjacent_lists[node.index]:
                if mins[adj_node] > node.distance+ :


n = 4, edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold = 4
