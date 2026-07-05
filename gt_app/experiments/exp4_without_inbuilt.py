import networkx as nx
import matplotlib.pyplot as plt
import math

def havel_hakimi_steps(seq):
    names = "ABCDEFGH"
    nodes = [[seq[i], names[i]] for i in range(len(seq))]
    G = nx.Graph()
    G.add_nodes_from(list(names))

    steps = []
    steps.append((G.copy(), [(n[1], n[0]) for n in nodes if n[0] >= 0], "Initial State"))
    while True:
        nodes.sort(key=lambda x: x[0], reverse=True)
        if nodes[0][0] == 0:
            break
        current_deg, current_name = nodes.pop(0)

        if current_deg > len(nodes):
            print(f"Error: {current_name} requires {current_deg} connections, but only {len(nodes)} nodes left.")
            return None
        print(f"Step: Connecting {current_name} (deg {current_deg})")

        for i in range(current_deg):
            adj_deg, adj_name = nodes[i]
            G.add_edge(current_name, adj_name)
            nodes[i][0] -= 1
            print(f"  - Created Edge: ({current_name}, {adj_name})")
            if nodes[i][0] < 0:
                print("Sequence is not graphical!")
                return None
        current_reqs = [(n[1], n[0]) for n in nodes]
        steps.append((G.copy(), current_reqs, f"After {current_name}"))
    return steps

seq = [5, 5, 4, 4, 3, 3, 2, 2]
if nx.is_graphical(seq):
    print("The sequence is Graphical. Processing steps...\n")
    all_steps = havel_hakimi_steps(seq)
    n_steps = len(all_steps)
    cols = 3
    rows = math.ceil(n_steps / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
    axes = axes.flatten()
    fixed_pos = nx.circular_layout("ABCDEFGH")

    for i in range(len(axes)):
        ax = axes[i]
        if i >= n_steps:
            ax.axis('off')
            continue
        current_G, reqs, title_text = all_steps[i]
        nx.draw(current_G, fixed_pos, ax=ax, with_labels=True,
                node_color='yellow', node_size=600,
                edge_color='black', width=1.5, font_weight='bold')
        req_str = ", ".join([f"{n}:{d}" for n, d in reqs if d >= 0])
        ax.set_title(f"{title_text}\nNeeds: [{req_str}]", fontsize=9)
    plt.tight_layout()
    plt.show()
else:
    print("The given sequence is not graphical.")