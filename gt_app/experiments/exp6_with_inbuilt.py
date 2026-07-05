import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
edges = [
    ("A", "C", 20),
    ("A", "B", 32),
    ("A", "D", 15),
    ("B", "D", 30),
    ("B", "G", 18),
    ("C", "D", 10),
    ("C", "F", 42),
    ("D", "F", 53),
    ("D", "E", 47),
    ("F", "E", 45),
    ("E", "G", 24),
    ("E", "H", 20),
    ("G", "H", 48),
]
G.add_weighted_edges_from(edges)
pos = nx.spring_layout(G, seed=42)
built_in_mst_edges = list(nx.minimum_spanning_edges(G, algorithm="kruskal", data=True))
fig, axes = plt.subplots(3, 3, figsize=(20, 10))
axes = axes.flatten()
mst_display_graph = nx.Graph()
mst_display_graph.add_nodes_from(G.nodes())

total_weight = 0
step = 0

for u, v, data in built_in_mst_edges:
    weight = data["weight"]
    ax = axes[step]
    mst_display_graph.add_edge(u, v, weight=weight)
    total_weight += weight
    nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=600, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=11, font_weight="bold", ax=ax)
    current_edges = list(mst_display_graph.edges())
    nx.draw_networkx_edges(G, pos, edgelist=current_edges, edge_color="darkgray", width=2, ax=ax)
    edge_labels = {(edge_u, edge_v): G[edge_u][edge_v]["weight"] for edge_u, edge_v in current_edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)
    ax.set_title(f"Step {step + 1}: Total Weight = {total_weight}", fontsize=14)
    ax.axis("off")
    step += 1
while step < len(axes):
    axes[step].axis("off")
    step += 1

plt.tight_layout()
plt.show()