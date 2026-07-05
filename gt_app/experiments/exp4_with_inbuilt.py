import networkx as nx
import matplotlib.pyplot as plt
import math

def get_havel_hakimi_steps(seq, names):
    if not nx.is_graphical(seq):
        print("Sequence is not graphical.")
        return None
    nodes = [[seq[i], names[i]] for i in range(len(seq))]
    G = nx.Graph()
    G.add_nodes_from(names)
    steps = []
    steps.append({
        'graph': G.copy(),
        'current': None,
        'targets': [],
        'title': "Initial State",
        'seq': [n[0] for n in nodes]
    })

    while True:
        nodes.sort(key=lambda x: x[0], reverse=True)
        if nodes[0][0] == 0:
            break
        current_deg, current_name = nodes.pop(0)
        new_edges = []
        target_names = []
        for i in range(current_deg):
            nodes[i][0] -= 1
            target_name = nodes[i][1]
            G.add_edge(current_name, target_name)
            new_edges.append((current_name, target_name))
            target_names.append(target_name)
        steps.append({
            'graph': G.copy(),
            'current': current_name,
            'targets': target_names,
            'new_edges': new_edges,
            'title': f"Connecting {current_name} (deg {current_deg})",
            'seq': [n[0] for n in nodes]
        })
    return steps

def havel_hakimi_trace(seq, names):
    if not nx.is_graphical(seq):
        print("The given sequence is not graphical.")
        return
    print("The sequence is Graphical. Processing steps...\n")
    nodes = [[seq[i], names[i]] for i in range(len(seq))]

    while True:
        nodes.sort(key=lambda x: x[0], reverse=True)
        if nodes[0][0] == 0:
            break
        current_deg, current_name = nodes.pop(0)
        print(f"Step: Connecting {current_name} (deg {current_deg})")
        for i in range(current_deg):
            nodes[i][0] -= 1
            target_name = nodes[i][1]
            print(f"  - Created Edge: ({current_name}, {target_name})")

sequence = [5, 5, 4, 4, 3, 3, 2, 2]
node_labels = "ABCDEFGH"
all_steps = get_havel_hakimi_steps(sequence, node_labels)
havel_hakimi_trace(sequence, node_labels)
if all_steps:
    n_steps = len(all_steps)
    cols = 3
    rows = math.ceil(n_steps / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
    axes = axes.flatten()

    pos = nx.circular_layout(node_labels)
    for i, step in enumerate(all_steps):
        ax = axes[i]
        G_step = step['graph']
        curr = step['current']
        targs = step['targets']
        all_edges = list(G_step.edges())
        new_edges = step.get('new_edges', [])
        old_edges = [e for e in all_edges if e not in new_edges and (e[1], e[0]) not in new_edges]
        nx.draw_networkx_edges(G_step, pos, ax=ax, edgelist=old_edges, edge_color='black', width=1)
        nx.draw_networkx_edges(G_step, pos, ax=ax, edgelist=new_edges, edge_color='black', width=1)
        nx.draw_networkx_nodes(G_step, pos, ax=ax, node_size=700, edgecolors='black')
        nx.draw_networkx_labels(G_step, pos, ax=ax, font_weight='bold')

        ax.set_title(f"Step {i}: {step['title']}\nRemaining Seq: {step['seq']}", fontsize=10)
        ax.axis('off')

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()