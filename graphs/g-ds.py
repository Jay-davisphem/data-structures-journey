'''
edges list + vertices list
v -> vertices,
e -> edges
Time complexity: O(e)
Space complexity: O(v + e)
'''

class Node(str):
    ...
vertices = ['A', 'B', 'C', 'D', 'E']

edges = [
    ['A', 'B'],
    ['A', 'D'],
    ['B', 'C'],
    ['C', 'D'],
    ['C', 'E'],
    ['D', 'E']
]


def find_adjacent_nodes(node: Node) -> list[Node]:
    '''
    Time: O(e)
    Returns list of adjacent nodes and None if node does't exist in vertices
    '''
    if node not in vertices:
        return None
    adj_nodes = []
    for cur_node, adj in edges:
        if node == cur_node:
            adj_nodes.append(adj)
        elif node == adj:
            adj_nodes.append(cur_node)

    return adj_nodes

def is_connected(node1: Node, node2: Node) -> bool:
    '''Time: O(e)'''
    if node1 not in vertices or node2 not in vertices:
        return False
    for edge in edges:
        if edge == [node1, node2] or edge == [node2, node1]:
            return True
    return False

print(find_adjacent_nodes('F'))
print(is_connected('C', 'E'))

'''
adjacency matrix -> visualize graph vividly
Space complexity: O(v^2)
'''

adjacency_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0],
]
vertices_idx = {vertices[i]: i for i in range(len(vertices)) }

def find_adjacency(node):
    '''Time: O(v)'''
    # get node row
    if node not in vertices:
        return None
    adjs = []
    idx = vertices_idx.get(node, None)
    if idx != None:
        for i, adj in enumerate(adjacency_matrix[idx]):
            if adj == 1:
                adjs.append(vertices[i])
    return adjs

def is_connected(node1, node2):
    '''Time: O(1)'''
    id1 = vertices_idx.get(node1, None)
    id2 = vertices_idx.get(node2, None)
    return False if id1 == None or id2 == None else bool(adjacency_matrix[id1][id2])
print(find_adjacency('C'))
print(is_connected('C', 'E'))

'''
adjacency list
'''


























