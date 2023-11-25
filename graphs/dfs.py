from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, val):
        node = Node(val)
        self.nodes[val] = node
                return dist

            for neighbor in self.nodes[node]:
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append((neighbor.val, dist + 1))


    def add_edge(self, src, dest):
        if src not in self.nodes:
            self.add_node(src)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[src].neighbors.append(self.nodes[dest])
        self.nodes[dest].neighbors.append(self.nodes[src])

                return dist

            for neighbor in self.nodes[node]:
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append((neighbor.val, dist + 1))

                return dist

            for neighbor in self.nodes[node]:
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append((neighbor.val, dist + 1))

    def shortest_path(self, start, end):
        if start not in self.nodes or end not in self.nodes:
            return None

        queue = deque([(start, 0)])
        visited = set([start])

                return dist

            for neighbor in self.nodes[node]:
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append((neighbor.val, dist + 1))

        while queue:
            node, dist = queue.popleft()
            if node == end:
                return dist

            for neighbor in self.nodes[node]:
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append((neighbor.val, dist + 1))

        return None