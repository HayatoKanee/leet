from collections import deque
from typing import List


def Edmonds_Karp(self, source: str, sink: str, graph) -> int:
    """1.residual network
       2.BFS
       3.Augmented path, if no exit"""

    pass


def backtrack(self, source, sink, parent):
    path = [sink]
    while path[-1] != source:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def bfs(self, source, sink, graph) -> List[str]:
    queue = deque([source])
    visited = set()
    parent = {}
    while queue:
        vertex = queue.popleft()
        if vertex == sink:
            return self.backtrack(source, sink, parent)
        if vertex not in visited:
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    parent[neighbour] = vertex
                    visited.add(neighbour)
    return []