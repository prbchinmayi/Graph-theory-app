import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
def create_graphs():
    G1 = nx.Graph()
    G1.add_nodes_from([1, 2, 3, 4, 5])
    e1_edges = [
        (1, 4), (1, 3),
        (5, 2), (5, 3),
        (4, 3),
        (2, 3)
    ]
    G1.add_edges_from(e1_edges)
    G2 = nx.Graph()
    G2.add_nodes_from([1, 2, 3, 4, 5, 6])
    e2_edges = [
        (1, 6), (1, 5),
        (6, 2), (6, 3), (6, 5),
        (5, 2), (5, 3),
        (2, 3), (2, 4),
        (3, 4)
    ]
    G2.add_edges_from(e2_edges)
    pos1 = {}
    angles1 = [90, 18, -54, -126, 162]
    for idx, node in enumerate([1, 2, 3, 4, 5]):
        angle_rad = np.radians(angles1[idx])
        pos1[node] = (np.cos(angle_rad), np.sin(angle_rad))
    pos2 = {
        1: (0, 1.4),
        6: (-1, 0.6),
        2: (1, 0.6),
        5: (-1, -0.6),
        3: (1, -0.6),
        4: (0, -1.3)
    }
    return [
        {"name": "Graph 1 (5 Nodes)", "G": G1, "pos": pos1},
        {"name": "Graph 2 (6 Nodes)", "G": G2, "pos": pos2}
    ]
def find_hamiltonian_backtracking(G):
    nodes = list(G.nodes())
    if not nodes:
        return None
    start_node = nodes[0]
    target_len = len(nodes)
    def backtrack(curr_node, path, visited):
        if len(path) == target_len:
            if G.has_edge(curr_node, start_node):
                return path + [start_node]
            return None
        for neighbor in G.neighbors(curr_node):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                result = backtrack(neighbor, path, visited)
                if result:
                    return result
                path.pop()
                visited.remove(neighbor)
        return None
    return backtrack(start_node, [start_node], {start_node})


def main():
    graphs = create_graphs()
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    for i, config in enumerate(graphs):
        G = config["G"]
        name = config["name"]
        pos = config["pos"]
        ax = axes[i]
        print(f"Finding Hamiltonian Cycle for {name} via Backtracking...")
        cycle = find_hamiltonian_backtracking(G)
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color='#ff8c5a', node_size=700, edgecolors='black', linewidths=2)
        nx.draw_networkx_labels(G, pos, ax=ax, font_size=12, font_weight='bold', font_color='black')
        nx.draw_networkx_edges(G, pos, ax=ax, edge_color='#ff8c5a', width=4)
        if cycle:
            print(f"{name}: Found Cycle -> {cycle}")
            edges = [(cycle[j], cycle[j + 1]) for j in range(len(cycle) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=edges, ax=ax, edge_color='blue', width=3, style='dashed')
            ax.set_title(f"{name}: Hamiltonian Cycle\n{cycle}", fontsize=12, fontweight='bold')
        else:
            print(f"{name}: No Hamiltonian Cycle found.")
            ax.set_title(f"{name}: No Hamiltonian Cycle", fontsize=12, fontweight='bold')
        ax.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()