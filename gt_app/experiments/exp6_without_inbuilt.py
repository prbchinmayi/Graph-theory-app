import networkx as nx
import matplotlib.pyplot as plt
import math

G = nx.Graph()
edges = [
    ('A', 'C', 20),
    ('A', 'B', 32),
    ('A', 'D', 15),
    ('B', 'D', 30),
    ('B', 'G', 18),
    ('C', 'D', 10),
    ('C', 'F', 42),
    ('D', 'F', 53),
    ('D', 'E', 47),
    ('F', 'E', 45),
    ('E', 'G', 24),
    ('E', 'H', 20),
    ('G', 'H', 48)
]

G.add_weighted_edges_from(edges)
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
parent = {node: node for node in G.nodes()}
rank = {node: 0 for node in G.nodes()}

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    ru, rv = find(u), find(v)
    if ru != rv:
        if rank[ru] > rank[rv]:
            parent[rv] = ru
        elif rank[ru] < rank[rv]:
            parent[ru] = rv
        else:
            parent[rv] = ru
            rank[ru] += 1
        return True
    return False

pos = {
    'D': (0, 0), 'E': (2, 0), 'G': (2, 2), 'H': (4.5, 0),
    'B': (-1.5, 2), 'A': (-2, -0.5), 'C': (-1.7, -2), 'F': (1.2, -1.7)
}

mst_edges = []
steps = []
for u, v, d in sorted_edges:
    if union(u, v):
        mst_edges.append((u, v, d['weight']))
        steps.append(list(mst_edges))
n = len(steps)
cols = 3
rows = math.ceil(n / cols)

fig, axes = plt.subplots(rows, cols, figsize=(15, 4 * rows))
axes = axes.flatten()
for i, current_edges in enumerate(steps):
    ax = axes[i]
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    total_weight = 0
    for u, v, w in current_edges:
        H.add_edge(u, v, weight=w)
        total_weight += w
    nx.draw(H, pos, ax=ax, with_labels=True,
            node_color='skyblue', node_size=600,
            font_size=10, font_weight='bold', edge_color='gray')
    labels = nx.get_edge_attributes(H, 'weight')
    nx.draw_networkx_edge_labels(H, pos, edge_labels=labels, ax=ax, font_size=9)
    ax.set_title(f"Step {i + 1}: Total Weight = {total_weight}")
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])
plt.tight_layout()
plt.show()
