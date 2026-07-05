import networkx as nx
import matplotlib.pyplot as plt

def apply_greedy_coloring(G, title, fixed_map=None):
    print(f"\n--- Coloring Trace for {title} ---")

    color_names = {
        0: 'Red',
        1: 'Blue',
        2: 'Green',
        3: 'Yellow'
    }
    color_hex = {
        0: '#FF4D4D',
        1: '#4D94FF',
        2: '#4DFF4D',
        3: '#FFFF4D'
    }
    sudoku_to_color_id = {'1': 0, '2': 1, '3': 2, '4': 3}
    def custom_strategy(graph, colors):
        if fixed_map:
            for node, val in fixed_map.items():
                colors[node] = sudoku_to_color_id[val]
        fixed_nodes = [n for n in graph.nodes() if fixed_map and n in fixed_map]
        rest_nodes = [n for n in graph.nodes() if fixed_map is None or n not in fixed_map]

        for node in fixed_nodes + rest_nodes:
            yield node

    color_dict = nx.greedy_color(G, strategy=custom_strategy)

    for node in sorted(G.nodes()):
        c_id = color_dict[node]
        c_name = color_names.get(c_id, f'Color-{c_id}')
        print(f"Vertex {node} -> assigned {c_name}")
    node_colors = [color_hex.get(color_dict[node], '#CCCCCC') for node in G.nodes()]
    chromatic_num = max(color_dict.values()) + 1
    print(f">> Minimal Chromatic Number achieved: {chromatic_num}")

    return node_colors, color_dict

G3 = nx.Graph()
for r in range(4):
    for c in range(4):
        G3.add_node((r, c))

row_straight, row_curved = [], []
col_straight, col_curved = [], []
block_edges = []

for r1 in range(4):
    for c1 in range(4):
        for r2 in range(4):
            for c2 in range(4):
                if (r1, c1) < (r2, c2):
                    if r1 == r2:
                        if abs(c1 - c2) == 1:
                            row_straight.append(((r1, c1), (r2, c2)))
                        else:
                            row_curved.append(((r1, c1), (r2, c2)))
                    elif c1 == c2:
                        if abs(r1 - r2) == 1:
                            col_straight.append(((r1, c1), (r2, c2)))
                        else:
                            col_curved.append(((r1, c1), (r2, c2)))
                    elif (r1 // 2 == r2 // 2) and (c1 // 2 == c2 // 2):
                        block_edges.append(((r1, c1), (r2, c2)))

G3.add_edges_from(row_straight + row_curved + col_straight + col_curved + block_edges)
pos3 = {(r, c): (c, -r) for r in range(4) for c in range(4)}

fixed_map = {
    (0, 2): '1',
    (1, 1): '1',
    (2, 2): '2'
}

colors_G3, cdict_G3 = apply_greedy_coloring(G3, "Graph G3 (Sudoku Graph)", fixed_map=fixed_map)

sudoku_number_map = {0: '1', 1: '2', 2: '3', 3: '4'}
labels_G3 = {node: sudoku_number_map.get(cdict_G3[node], '?') for node in G3.nodes()}

fig, ax = plt.subplots(figsize=(8, 8))
fig.suptitle("Greedy Graph Colouring Algorithm", fontsize=16, fontweight='bold')
ax.set_title("Graph G3 (4x4 Sudoku Graph)")


nx.draw_networkx_edges(G3, pos3, ax=ax, edgelist=row_straight, edge_color='#2ca02c', width=1.5)
nx.draw_networkx_edges(G3, pos3, ax=ax, edgelist=col_straight, edge_color='#d62728', width=1.5)
nx.draw_networkx_edges(G3, pos3, ax=ax, edgelist=block_edges, edge_color='#1f77b4', width=1.5)

G_directed = nx.DiGraph(G3)
for u, v in row_curved:
    rad = 0.4 if u[0] < 2 else -0.4
    nx.draw_networkx_edges(G_directed, pos3, ax=ax, edgelist=[(u, v)],
                           edge_color='#2ca02c', width=1.5,
                           connectionstyle=f"arc3,rad={rad}",
                           arrows=True, arrowstyle='-')

for u, v in col_curved:
    rad = -0.4 if u[1] < 2 else 0.4
    nx.draw_networkx_edges(G_directed, pos3, ax=ax, edgelist=[(u, v)],
                           edge_color='#d62728', width=1.5,
                           connectionstyle=f"arc3,rad={rad}",
                           arrows=True, arrowstyle='-')

nx.draw_networkx_nodes(G3, pos3, ax=ax, node_color=colors_G3, node_size=800)
nx.draw_networkx_labels(G3, pos3, labels=labels_G3, ax=ax, font_size=16, font_weight='bold')

ax.axis('off')
plt.tight_layout()
plt.show()