import matplotlib.pyplot as plt
import networkx as nx
import math
def draw_step_on_ax(ax, G_orig, pos, current_node, traversed_edges, step_num, total_steps):
    ax.set_aspect('equal')
    for u, v in G_orig.edges:
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color='#E0E0E0', linewidth=2, zorder=1)
    for idx, (u, v) in enumerate(traversed_edges):
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        is_latest = (idx == len(traversed_edges) - 1)
        color = 'crimson' if is_latest else 'indigo'
        linewidth = 4.5 if is_latest else 3.5
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=linewidth, alpha=0.9, zorder=2)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mx, my + 0.04, f"#{idx + 1}", color='white', weight='bold', fontsize=8,
                bbox=dict(facecolor=color, edgecolor='none', boxstyle='circle,pad=0.15'), zorder=4)

    for node in G_orig.nodes:
        if node == current_node:
            n_color = '#32CD32'
            size = 700
        elif any(node in edge for edge in traversed_edges):
            n_color = 'gold'
            size = 550
        else:
            n_color = 'lightgrey'
            size = 550

        ax.scatter(pos[node][0], pos[node][1], color=n_color, s=size, edgecolors='black', linewidths=1.2, zorder=5)
        ax.text(pos[node][0], pos[node][1], str(node), color='black', weight='bold', ha='center', va='center', zorder=6,
                fontsize=10)
    ax.set_title(f"Step {step_num}/{total_steps}", fontweight='bold', pad=8, fontsize=11)
    ax.axis('off')

edges_G1 = [(1, 3), (1, 4), (2, 3), (2, 5), (3, 4), (3, 5)]
edges_G2 = [(1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (5, 6)]
graphs = [
    {"name": "Graph 1", "G": nx.Graph(edges_G1)},
    {"name": "Graph 2", "G": nx.Graph(edges_G2)}
]

for idx, graph_data in enumerate(graphs):
    G = graph_data["G"]
    g_name = graph_data["name"]
    print(f"{'=' * 60}\nANALYZING {g_name.upper()}\n{'=' * 60}")
    if not nx.is_eulerian(G):
        odd_vertices = [u for u in G.nodes if G.degree(u) % 2 != 0]
        print(f"-> Status: SKIPPING PLOT — Eulerian CIRCUIT is not possible.")
        print(f"   Reason: Every vertex must have an even degree.")
        print(f"   Your graph has {len(odd_vertices)} vertices with odd degrees: {odd_vertices}\n")
        continue
    print("-> Status: Valid Eulerian CIRCUIT Found! (All nodes have even degrees)\n")
    sorted_nodes = sorted(list(G.nodes))
    n = len(sorted_nodes)
    pos = {}
    for i_node, node in enumerate(sorted_nodes):
        angle = math.pi / 2 - (2 * math.pi * i_node / n)
        pos[node] = (math.cos(angle), math.sin(angle))
    start_node = sorted_nodes[0]
    edges_to_traverse = list(nx.eulerian_circuit(G, source=start_node))
    steps_data = []
    tour_edges = []
    tour_nodes = [start_node]
    total_expected_steps = len(edges_to_traverse)
    for step, (u, v) in enumerate(edges_to_traverse, start=1):
        print(f"  Step {step:02d}: At Node {u} -> Traveled Edge ({u}, {v})")
        tour_edges.append((u, v))
        tour_nodes.append(v)
        steps_data.append((v, list(tour_edges), step))
    print(f"\nSUCCESS: Eulerian Circuit Sequence: {' -> '.join(map(str, tour_nodes))}\n")
    cols = 3
    rows = math.ceil(total_expected_steps / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(15, 4.5 * rows))
    if rows == 1:
        axes = [axes] if cols == 1 else list(axes)
    else:
        axes = axes.flatten()
    for i in range(len(axes)):
        if i < len(steps_data):
            c_node, t_edges, s_num = steps_data[i]
            draw_step_on_ax(axes[i], G, pos, c_node, t_edges, s_num, total_expected_steps)
        else:
            axes[i].axis('off')
    plt.suptitle(f"NetworkX Eulerian Circuit Steps ({g_name})", fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.show()