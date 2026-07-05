import networkx as nx
import matplotlib.pyplot as plt
import math

G = nx.Graph()
edges = [
    ('A', 'B', 6), ('A', 'C', 10), ('A', 'F', 3), ('A', 'G', 6),
    ('B', 'F', 2), ('C', 'D', 7), ('C', 'G', 1),
    ('D', 'E', 3), ('D', 'G', 5), ('D', 'H', 4),
    ('E', 'H', 4), ('F', 'G', 1), ('G', 'H', 9)
]
G.add_weighted_edges_from(edges)
pos = {
    'A': (1, 2), 'B': (0, 1), 'C': (2, 1),
    'F': (1, 0), 'G': (2, 0), 'D': (3, 2),
    'H': (4, 1), 'E': (5, 2)
}

source = 'A'
all_paths = nx.single_source_dijkstra_path(G, source)
all_distances = nx.single_source_dijkstra_path_length(G, source)
targets = sorted([node for node in G.nodes() if node != source])

n_targets = len(targets)
cols = 3
rows = math.ceil(n_targets / cols)
fig, axes = plt.subplots(rows, cols, figsize=(15, 4 * rows))
axes = axes.flatten()

print(f"Step-by-Step Shortest Paths from {source}:\n" + "-" * 35)
for i, target in enumerate(targets):
    ax = axes[i]
    path = all_paths[target]
    dist = all_distances[target]
    path_edges = list(zip(path, path[1:]))

    nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.1, edge_color='gray')
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color='#eeeeee', node_size=400)
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=path_edges,
                           edge_color='green', width=3)
    node_colors = []
    for node in G.nodes():
        if node in path:
            node_colors.append('skyblue')
        else:
            node_colors.append('#eeeeee')

    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors, node_size=400, edgecolors='black')
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_weight='bold')

    path_weight_labels = {(u, v): G[u][v]['weight'] for u, v in path_edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=path_weight_labels, ax=ax, font_color='green')
    print(f"To {target}: {' -> '.join(path)} | Total Weight: {dist}")
    ax.set_title(f"Shortest Path: {source} to {target}\nTotal Distance: {dist}", fontsize=11)
    ax.axis('off')

for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()