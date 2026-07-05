import matplotlib.pyplot as plt
import networkx as nx
import math

def get_edges_from_path(path):
    return [tuple(sorted((path[i], path[i + 1]))) for i in range(len(path) - 1)]

def find_max_closed_trail(G):
    global_max_trail = []
    for start_node in G.nodes():
        stack = [(start_node, [], set())]
        while stack:
            curr, path, used_edges = stack.pop()
            if curr == start_node and len(path) > len(global_max_trail):
                global_max_trail = path + [start_node]
            for neighbor in G.neighbors(curr):
                edge = tuple(sorted((curr, neighbor)))
                if edge not in used_edges:
                    new_used = used_edges.copy()
                    new_used.add(edge)
                    stack.append((neighbor, path + [curr], new_used))
    return global_max_trail

def plot_substructure(ax, G, pos, nodes, edges, color, title, is_walk=False):
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color='grey', node_size=600)
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color='black', width=2)
    if nodes:
        nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=set(nodes),
                               node_color=color, node_size=600, edgecolors='black')
        if not is_walk:
            nx.draw_networkx_edges(G, pos, ax=ax, edgelist=edges, edge_color=color, width=3)
        else:
            edge_counts = {}
            for edge in edges:
                edge_counts[edge] = edge_counts.get(edge, 0) + 1
            for edge, count in edge_counts.items():
                if count == 1:
                    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=[edge], edge_color=color, width=3)
                else:
                    for i in range(count):
                        rad = 0.2 * (i + 1)
                        nx.draw_networkx_edges(G, pos, ax=ax, edgelist=[edge],
                                               edge_color=color, width=3,
                                               connectionstyle=f"arc3,rad={rad}")

    nx.draw_networkx_labels(G, pos, ax=ax, font_weight='bold')
    ax.set_title(title, fontweight='bold', pad=10)
    ax.axis('off')

G1 = nx.Graph([(1, 3), (1, 4), (2, 3), (2, 5), (3, 4), (3, 5)])
G2 = nx.Graph([(1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (5, 6)])

graphs = [G1, G2]
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

for i, G in enumerate(graphs):
    print(f"=== GRAPH {i + 1} RESULTS ===")

    # Sort nodes numerically and calculate circular coordinates starting from the top
    sorted_nodes = sorted(list(G.nodes()))
    n = len(sorted_nodes)
    pos = {}
    for idx, node in enumerate(sorted_nodes):
        angle = math.pi / 2 - (2 * math.pi * idx / n)
        pos[node] = (math.cos(angle), math.sin(angle))

    # --- PATH (Max Cycle) ---
    cycles = list(nx.simple_cycles(G.to_directed()))
    max_cyc = max([c for c in cycles if len(c) > 2], key=len) + [max([c for c in cycles if len(c) > 2], key=len)[0]]
    plot_substructure(axes[i, 0], G, pos, max_cyc, get_edges_from_path(max_cyc), 'skyblue', "PATH\n(Max Cycle)")
    print(f"Max Cycle (Path):       {' -> '.join(map(str, max_cyc))}")

    # --- TRAIL (Max Circuit) ---
    trail = find_max_closed_trail(G)
    plot_substructure(axes[i, 1], G, pos, trail, get_edges_from_path(trail), 'lightgreen', "TRAIL\n(Max Circuit)")
    print(f"Max Circuit (Trail):    {' -> '.join(map(str, trail))}")

    # --- WALK (Max closed covering) ---
    walk_edges = list(nx.eulerian_circuit(nx.eulerize(G)))
    walk_nodes = [u for u, v in walk_edges] + [walk_edges[-1][1]]
    plot_substructure(axes[i, 2], G, pos, walk_nodes, walk_edges, 'coral', "WALK\n(Max closed covering)", is_walk=True)
    print(f"Max Closed Walk:    {' -> '.join(map(str, walk_nodes))}\n")

plt.tight_layout()
plt.show()