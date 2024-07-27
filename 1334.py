import heapq
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjacent_lists = self.initialise(n, edges)
        source = 0
        min_count = n + 1
        for i in range(n):
            parent = self.dijkstra(n, i, distanceThreshold, adjacent_lists)
            count = self.count_parent(parent)
            if count <= min_count:
                min_count = count
                source = i
        return source

    def initialise(self, n: int, edges: List[List[int]]):
        adjacent_lists = []
        for i in range(n):
            adjacent_lists.append([])
        for edge in edges:
            # edge is [startnode, endnode, weight]
            startnode = edge[0]
            endnode = edge[1]
            weight = edge[2]
            adjacent_lists[startnode].append((endnode, weight))
            adjacent_lists[endnode].append((startnode, weight))
        return adjacent_lists

    def dijkstra(self, n: int, source: int, distanceThreshold: int, adjacent_lists: List[List[int]]) -> List[int]:
        parent = []
        mins = []
        for i in range(n):
            parent.append(-1)
            if source != i:
                mins.append(distanceThreshold + 1)
            else:
                mins.append(0)
        """if node 0 is the source, initital queue would be 
        [(0,-1,0),(1,-1, 2),(2,-1, inf), (3,-1, inf), (4,-1, 8)]"""
        queue = [(mins[i], i) for i in range(n)]
        heapq.heapify(queue)
        while queue:
            node = heapq.heappop(queue)[1]
            for adj_node in adjacent_lists[node]:
                w = mins[node] + adj_node[1]
                if mins[adj_node[0]] > w and w <= distanceThreshold:
                    mins[adj_node[0]] = w
                    parent[adj_node[0]] = node
                    heapq.heappush(queue, (w, adj_node[0]))
        return parent

    def count_parent(self, parent:List[int]):
        count = 0
        for node in parent:
            if node != -1:
                count += 1
        return count
# n = 5
# edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
# distanceThreshold = 2
# solution = Solution()
# print(solution.findTheCity(n, edges, distanceThreshold))
