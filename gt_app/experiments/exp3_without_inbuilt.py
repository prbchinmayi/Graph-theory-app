import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()
outer_nodes = [1, 2, 3, 4, 5, 6, 7]
inner_nodes = [8, 12, 9, 10, 11]
G.add_nodes_from(outer_nodes + inner_nodes)
edges = [
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 1),
    (1, 8), (8, 12), (6, 12), (12, 3),
    (2, 9), (9, 10), (10, 11), (4, 11), (5, 11), (7, 9),
    (8, 10)
]
G.add_edges_from(edges)

pos = {
    1: (0, 2.5), 2: (1.8, 1.5), 3: (1.8, -0.9), 4: (1.1, -2),
    5: (-1.1, -2), 6: (-1.8, -0.9), 7: (-1.8, 1.5),
    8: (-0.8, 0.8), 12: (-0.8, -0.4),
    9: (0, 1.2), 10: (0, 0), 11: (0, -1.2)
}

def manual_bfs_tree(graph, start):
    visited = set()
    queue = deque([start])
    tree_edges = []
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                tree_edges.append((node, neighbor))

    T = nx.Graph()
    T.add_edges_from(tree_edges)
    return T
spanning_G = manual_bfs_tree(G, 1)

selected_edges = [(8, 12), (12, 3), (9, 10), (10, 11), (8, 10)]
edge_induced_G = nx.Graph()
for u, v in selected_edges:
    if G.has_edge(u, v):
        edge_induced_G.add_edge(u, v)

selected_nodes = [1, 2, 7, 8, 9, 12]
node_induced_G = nx.Graph()
node_induced_G.add_nodes_from(selected_nodes)
for u, v in G.edges():
    if u in selected_nodes and v in selected_nodes:
        node_induced_G.add_edge(u, v)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
graphs = [
    (G, "Original Graph", 'crimson'),
    (spanning_G, "Spanning Subgraph", 'lightblue'),
    (edge_induced_G, "Edge-Induced", 'gold'),
    (node_induced_G, "Node-Induced", 'lightgreen')
]
for ax, (graph, title, color) in zip(axes.flatten(), graphs):
    nx.draw(graph, pos, with_labels=True, node_color=color,
            node_size=600, edge_color='black', ax=ax)
    ax.set_title(title)
    ax.axis('off')
plt.tight_layout()
plt.show()