import networkx as nx

G = nx.Graph()
stations = ["Airport", "Railway", "River", "University", "Center", "Market", "Park", "Lake"]
edges = [
    ("Airport", "Railway"),
    ("Railway", "River"),
    ("Railway", "University"),
    ("University", "Center"),
    ("Center", "Park"),
    ("Park", "Lake"),
    ("Lake", "Airport"),
    ("Airport", "Center"),
    ("Center", "Market")
]
G.add_nodes_from(stations)
G.add_edges_from(edges)


def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(
                neighbor
                for neighbor in graph.neighbors(vertex)
                if neighbor not in visited
            )
    return path


def bfs(graph, start):
    visited = set()
    queue = [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(
                neighbor
                for neighbor in graph.neighbors(vertex)
                if neighbor not in visited
            )
    return path


start_node = "Market"
dfs_path = dfs(G, start_node)
bfs_path = bfs(G, start_node)

print("DFS Path:", dfs_path)
print("BFS Path:", bfs_path)