import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6])
edges = [
    (1, 2),
    (1, 4),
    (1, 6),
    (2, 3),
    (2, 5),
    (3, 4),
    (3, 5),
    (3, 6),
    (4, 5),
    (5, 6),
]
G.add_edges_from(edges)
coloring = nx.coloring.greedy_color(G, strategy="largest_first")
num_colors = len(set(coloring.values()))

print("Greedy Coloring Result:")
for node in sorted(G.nodes()):
    print(f"Vertex {node} : Color {coloring[node]}")
print(f"\nTotal colors used: {num_colors}")
color_map = {
    0: "red",
    1: "blue",
    2: "green",
    3: "yellow"
}
node_colors = [color_map[coloring[node]] for node in G.nodes()]
pos = {
    1: np.array([0.0, 4.0]),
    2: np.array([0.5, 1.75]),
    3: np.array([-0.45, 0.0]),
    4: np.array([-2.0, 4.0]),
    5: np.array([-2.5, 2.0]),
    6: np.array([-2.45, 0.0]),
}

angle = np.pi / 2
rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
for node in pos:
    pos[node] = rotation_matrix @ pos[node]

plt.figure(figsize=(6, 6))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=800,
    font_color="white",
    font_weight="bold",
)
plt.title("Greedy Graph Coloring")
plt.show()