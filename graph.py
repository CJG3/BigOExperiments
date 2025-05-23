from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = [s]

        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s)

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.add_edge(3, 5)


g.bfs(2)


