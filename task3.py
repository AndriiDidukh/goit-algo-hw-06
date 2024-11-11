import heapq
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
stations = ["Airport", "Railway", "River", "University", "Center", "Market", "Park", "Lake"]
edges = {
    ("Airport", "Railway", 1),
    ("Railway", "University", 4),
    ("University", "Center", 1),
    ("Center", "Park", 3),
    ("Park", "Lake", 2),
    ("Lake", "Airport", 2),
    ("Airport", "Center", 5),
    ("Center", "Market", 1),
    ("Railway", "River", 1),
}
G.add_nodes_from(stations)
G.add_weighted_edges_from(edges)


def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, attributes in graph[current_node].items():
            weight = attributes["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


all_distances = {node: dijkstra(G, node) for node in G.nodes}


print("Shortest distances between all stations:")
for source in all_distances:
    for target in all_distances[source]:
        print(f"From {source} To {target}: Distance {all_distances[source][target]}")


pos = nx.circular_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="yellow",
    node_size=2000,
    edge_color="black",
    font_size=14,
    font_color="black",
)


edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
