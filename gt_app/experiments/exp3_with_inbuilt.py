import networkx as nx
import matplotlib.pyplot as plt

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
spanning_G = nx.bfs_tree(G, source=1).to_undirected()

selected_edges = [(8, 12), (12, 3), (9, 10), (10, 11), (8, 10)]
edge_induced_G = G.edge_subgraph(selected_edges).copy()

selected_nodes = [1, 2, 7, 8, 9, 12]
node_induced_G = G.subgraph(selected_nodes).copy()

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
plt.subplots_adjust(wspace=0.3, hspace=0.3)

graphs = [
    (G, "Original Graph", 'crimson'),
    (spanning_G, "Spanning Subgraph", 'lightblue'),
    (edge_induced_G, "Edge-Induced", 'gold'),
    (node_induced_G, "Node-Induced", 'lightgreen')
]
for ax, (graph, title, color) in zip(axes.flatten(), graphs):
    nodelist = list(graph.nodes())
    nx.draw_networkx_nodes(graph, pos, nodelist=nodelist, node_color=color, node_size=600, ax=ax)
    nx.draw_networkx_edges(graph, pos, width=2, edge_color='black', ax=ax)
    nx.draw_networkx_labels(graph, pos, font_size=10, font_weight='bold', ax=ax)

    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.axis('off')

plt.tight_layout()
plt.show()