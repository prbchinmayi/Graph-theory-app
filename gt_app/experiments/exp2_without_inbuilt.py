import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def analyze_isomorphism(G1, G2, pair_name):
    v1, v2 = G1.number_of_nodes(), G2.number_of_nodes()
    e1, e2 = G1.number_of_edges(), G2.number_of_edges()
    d1_dict = dict(G1.degree())
    d2_dict = dict(G2.degree())
    d1_seq = sorted(d1_dict.values(), reverse=True)
    d2_seq = sorted(d2_dict.values(), reverse=True)
    c1 = nx.cycle_basis(G1)
    c2 = nx.cycle_basis(G2)

    def get_cycle_info(G, cycles, deg_dict):
        paths = []
        for cycle in cycles:
            paths.append(sorted([deg_dict[node] for node in cycle]))
        return sorted(paths)
    path1 = get_cycle_info(G1, c1, d1_dict)
    path2 = get_cycle_info(G2, c2, d2_dict)
    nodes_match = (v1 == v2)
    edges_match = (e1 == e2)
    degrees_match = (d1_seq == d2_seq)
    cycle_count_match = (len(c1) == len(c2))
    cycle_paths_match = (path1 == path2)

    def manual_find_mapping(g1, g2):
        if not (nodes_match and edges_match and degrees_match):
            return None

        mapping = {}
        g2_nodes_available = list(g2.nodes())
        for n1 in g1.nodes():
            deg1 = g1.degree(n1)
            neighbors_degs1 = sorted([g1.degree(nb) for nb in g1.neighbors(n1)])
            found = False
            for n2 in g2_nodes_available:
                deg2 = g2.degree(n2)
                neighbors_degs2 = sorted([g2.degree(nb) for nb in g2.neighbors(n2)])
                if deg1 == deg2 and neighbors_degs1 == neighbors_degs2:
                    mapping[n1] = n2
                    g2_nodes_available.remove(n2)
                    found = True
                    break
            if not found: return None

        for u, v in g1.edges():
            if not g2.has_edge(mapping[u], mapping[v]):
                return None
        return mapping
    mapping = manual_find_mapping(G1, G2)

    print(f"\n------------- ANALYSIS: {pair_name} -----------")
    print(f"Graph 1: Vertices={v1}, Edges={e1}")
    print(f"Graph 2: Vertices={v2}, Edges={e2}")
    print(f"Nodes Match: {nodes_match}")
    print(f"Edges Match: {edges_match}")
    print(f"G1 Degree Sequence: {d1_seq}")
    print(f"G2 Degree Sequence: {d2_seq}")
    print(f"Degree Sequence Match: {degrees_match}")
    print(f"Cycle Count: G1={len(c1)}, G2={len(c2)}")
    print(f"Cycle Count Match: {cycle_count_match}")
    print(f"Cycle Path: G1={path1}")
    print(f"            G2={path2}")
    print(f"Cycle Degree Paths Match: {cycle_paths_match}")
    print(f"FINAL ISOMORPHISM STATUS: {'ISOMORPHIC' if mapping else 'NOT ISOMORPHIC'}")
    if mapping:
        print(f"Manual Node Mapping: {mapping}")

G1_a = nx.Graph()
G1_a.add_edges_from([('a', 'c'), ('c', 'e'), ('e', 'b'), ('b', 'd'), ('d', 'a')])
G1_b = nx.Graph()
G1_b.add_edges_from([('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '1')])
G2_a = nx.Graph()
G2_a.add_edges_from([('a', 'b'), ('b', 'h'), ('h', 'g'), ('g', 'a'),
                     ('c', 'd'), ('d', 'f'), ('f', 'e'), ('e', 'c'),
                     ('a', 'd'), ('g', 'f')])
G2_b = nx.Graph()
G2_b.add_edges_from([('1', '2'), ('2', '3'), ('3', '4'), ('4', '1'),
                     ('5', '6'), ('6', '7'), ('7', '8'), ('8', '5'),
                     ('1', '5'), ('4', '7')])

G3_a = nx.Graph()
outer_nodes = range(8)
inner_nodes = range(8, 16)
for i in range(8):
    G3_a.add_edge(i, (i + 1) % 8)
for i in range(8, 16):
    next_inner = 8 + (i - 8 + 3) % 8
    G3_a.add_edge(i, next_inner)
for i in range(8):
    G3_a.add_edge(i, i + 8)

pos3a = {}
for i in range(8):
    angle = np.pi / 2 - i * (2 * np.pi / 8)
    pos3a[i] = np.array([np.cos(angle), np.sin(angle)])

radius_inner = 0.5
for i in range(8, 16):
    angle = np.pi / 2 - (i - 8) * (2 * np.pi / 8)
    pos3a[i] = np.array([radius_inner * np.cos(angle), radius_inner * np.sin(angle)])

G3_b = nx.Graph()
inner_shell = range(0, 8)
outer_shell = range(8, 16)
G3_b .add_nodes_from(inner_shell)
G3_b.add_nodes_from(outer_shell)
G3_b.add_edges_from([(i, (i + 4) % 8) for i in range(8)])
G3_b.add_edges_from([(i, (i+8)) for i in range(8)])
G3_b.add_edges_from([(i, (i+7)) for i in range(1,8)])
G3_b.add_edges_from([(0,15)])
curved_edges = [(8,11),(10,13),(12,15),(14,9)]
G3_b.add_edges_from(curved_edges)

pos3b = {}
radius_outer = 0.3
radius_inner = 0.15
base_angles = [(np.pi / 2 - i * (2 * np.pi / 8)) for i in range(8)]

for i in range(8):
    angle = base_angles[i]
    pos3b[inner_shell[i]] = np.array([radius_inner * np.cos(angle), radius_inner * np.sin(angle)])
    pos3b[outer_shell[i]] = np.array([radius_outer * np.cos(angle-np.pi/8), radius_outer * np.sin(angle-np.pi/8)])

G3_c = nx.Graph()
nodes = range(16)
G3_c.add_nodes_from(nodes)
G3_c.add_edges_from([(i, (i + 1) % 16) for i in range(16)])
G3_c.add_edges_from([(0,11),(1,6),(2,13),(3,8),(4,15),(5,10),(7,12),(9,14)])
pos3c = {}
for i in range(16):
    angle = np.pi / 2 - i * (2 * np.pi / 16)
    pos3c[i] = np.array([np.cos(angle), np.sin(angle)])

analyze_isomorphism(G1_a, G1_b, "QUESTION 1")
analyze_isomorphism(G2_a, G2_b, "QUESTION 2")
analyze_isomorphism(G3_a, G3_b, "QUESTION 3A:3a&3b")
analyze_isomorphism(G3_a, G3_c, "QUESTION 3B:3a&3c")
plt.figure(figsize=(12, 12))

plt.subplot(3, 3, 1)
pos1a = nx.circular_layout(['a', 'b', 'c', 'd', 'e'])
nx.draw(G1_a, pos1a, with_labels=True, node_color='lightblue', node_size=800)
plt.title("Q1: Graph A (Star Path)")
plt.subplot(3, 3, 2)
pos1b = nx.circular_layout(['1', '2', '3', '4', '5'])
nx.draw(G1_b, pos1b, with_labels=True, node_color='lightgreen', node_size=800)
plt.title("Q1: Graph B (Pentagon)")

plt.subplot(3, 3, 4)
pos2a = {'a': (-2, 2), 'b': (2, 2), 'h': (2, -2), 'g': (-2, -2),
         'd': (-1, 1), 'c': (1, 1), 'e': (1, -1), 'f': (-1, -1)}
nx.draw(G2_a, pos2a, with_labels=True, node_color='lightblue', node_size=800)
plt.title("Q2: Graph A")
plt.subplot(3, 3, 5)
pos2b = {'1': (-2, 2), '2': (2, 2), '3': (2, -2), '4': (-2, -2),
         '5': (-1, 1), '6': (1, 1), '7': (1, -1), '8': (-1, -1)}
nx.draw(G2_b, pos2b, with_labels=True, node_color='lightgreen', node_size=800)
plt.title("Q2: Graph B ")

plt.subplot(3, 3, 7)
nx.draw(G3_a, pos3a, with_labels=True, node_color='lightblue', node_size=300)
plt.title("Q3: Graph A")
plt.subplot(3, 3, 8)
nx.draw(G3_b, pos3b, with_labels=True, node_color='lightblue', node_size=300)
nx.draw_networkx_edges(
    G3_b, pos3b,
    edgelist=curved_edges,
    connectionstyle="arc3,rad=-1.1",
    arrows=True,
    arrowsize=0,
    edge_color='black'
)
plt.title("Q3: Graph B")
plt.subplot(3, 3, 9)
nx.draw(G3_c, pos3c, with_labels=True, node_color='lightblue', node_size=300)
plt.title("Q3: Graph C")

plt.tight_layout()
plt.show()
