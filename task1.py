import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
stations = ["Airport", "Railway", "River", "University", "Center", "Market", "Park", "Lake"]
G.add_nodes_from(stations)

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

G.add_edges_from(edges)
pos = nx.circular_layout(G)

edge_labels = {
    ("Airport", "Railway"): "1",
    ("Railway", "University"): "2",
    ("University", "Center"): "3",
    ("Center", "Park"): "4",
    ("Park", "Lake"): "5",
    ("Lake", "Airport"): "6",
    ("Airport", "Center"): "7",
    ("Center", "Market"): "8",
    ("Railway", "River"): "9"
}

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

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color="red",
    font_size=12,
)

plt.title("Invented traffic scheme:")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)


print(f"Nodes Number: {num_nodes}")
print(f"Edges Number: {num_edges}")
print("Nodes degree:")
for node, degree in degree_centrality.items():
    print(f"{node}: {degree:.2f}")
