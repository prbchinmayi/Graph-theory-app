import matplotlib.pyplot as plt
import networkx as nx
import math

def get_edges_from_path(path):
    return [tuple(sorted((path[i], path[i + 1]))) for i in range(len(path) - 1)]
def find_max_cycle_scratch(G):
    best_cycle = []
    nodes = list(G.nodes())
    for start_node in nodes:
        stack = [(start_node, [start_node], set())]
        while stack:
            curr, path, visited_edges = stack.pop()

            for neighbor in G.neighbors(curr):
                edge = tuple(sorted((curr, neighbor)))
                if neighbor == start_node and len(path) >= 3:
                    if len(path) + 1 > len(best_cycle):
                        best_cycle = path + [start_node]
                if neighbor not in path and edge not in visited_edges:
                    new_edges = visited_edges.copy()
                    new_edges.add(edge)
                    stack.append((neighbor, path + [neighbor], new_edges))
    return best_cycle

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

def bfs_shortest_path(G, start, end):
    queue = [[start]]
    visited = {start}
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return []

def find_max_closed_walk_scratch(G):
    odd_nodes = [v for v in G.nodes() if G.degree(v) % 2 != 0]
    adj_multigraph = {v: list(G.neighbors(v)) for v in G.nodes()}

    if odd_nodes:
        odd_working = odd_nodes.copy()
        while odd_working:
            u = odd_working.pop(0)
            v = odd_working.pop(0)

            path = bfs_shortest_path(G, u, v)
            for i in range(len(path) - 1):
                n1, n2 = path[i], path[i + 1]
                adj_multigraph[n1].append(n2)
                adj_multigraph[n2].append(n1)

    start_vertex = list(G.nodes())[0]
    curr_path = [start_vertex]
    circuit = []

    active_edges = {v: adj_multigraph[v].copy() for v in adj_multigraph}

    while curr_path:
        curr_v = curr_path[-1]
        if active_edges[curr_v]:
            next_v = active_edges[curr_v].pop(0)
            active_edges[next_v].remove(curr_v)
            curr_path.append(next_v)
        else:
            circuit.append(curr_path.pop())
    circuit.reverse()
    final_edges = [(circuit[i], circuit[i + 1]) for i in range(len(circuit) - 1)]
    return circuit, final_edges
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
                sorted_e = tuple(sorted(edge))
                edge_counts[sorted_e] = edge_counts.get(sorted_e, 0) + 1
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
    sorted_nodes = sorted(list(G.nodes()))
    n = len(sorted_nodes)
    pos = {}
    for idx, node in enumerate(sorted_nodes):
        angle = math.pi / 2 - (2 * math.pi * idx / n)
        pos[node] = (math.cos(angle), math.sin(angle))
    max_cyc = find_max_cycle_scratch(G)
    plot_substructure(axes[i, 0], G, pos, max_cyc, get_edges_from_path(max_cyc), 'skyblue', "PATH\n(Max Cycle)")
    print(f"Max Cycle (Path):       {' -> '.join(map(str, max_cyc))}")
    trail = find_max_closed_trail(G)
    plot_substructure(axes[i, 1], G, pos, trail, get_edges_from_path(trail), 'lightgreen', "TRAIL\n(Max Circuit)")
    print(f"Max Circuit (Trail):    {' -> '.join(map(str, trail))}")
    walk_nodes, walk_edges = find_max_closed_walk_scratch(G)
    plot_substructure(axes[i, 2], G, pos, walk_nodes, walk_edges, 'coral', "WALK\n(Max closed covering)", is_walk=True)
    print(f"Max Closed Walk:    {' -> '.join(map(str, walk_nodes))}\n")

plt.tight_layout()
plt.show()