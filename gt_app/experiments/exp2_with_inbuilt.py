import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def analyze_isomorphism_builtin(G1, G2, pair_name):
    isomorphic = nx.is_isomorphic(G1, G2)
    matcher = nx.algorithms.isomorphism.GraphMatcher(G1, G2)
    mapping = matcher.mapping if isomorphic else None
    print(f"\n------------- ANALYSIS: {pair_name} -----------")
    print(f"Graph 1: Nodes={G1.number_of_nodes()}, Edges={G1.number_of_edges()}")
    print(f"Graph 2: Nodes={G2.number_of_nodes()}, Edges={G2.number_of_edges()}")
    d1_seq = sorted([d for n, d in G1.degree()], reverse=True)
    d2_seq = sorted([d for n, d in G2.degree()], reverse=True)
    print(f"Degree Sequences Match: {d1_seq == d2_seq}")
    print(f"FINAL ISOMORPHISM STATUS: {'ISOMORPHIC' if isomorphic else 'NOT ISOMORPHIC'}")
    if mapping:
        print(f"Mapping Found: {mapping}")

G1_a = nx.Graph([('a', 'c'), ('c', 'e'), ('e', 'b'), ('b', 'd'), ('d', 'a')])
G1_b = nx.cycle_graph(5);
G1_b = nx.relabel_nodes(G1_b, {i: str(i + 1) for i in range(5)})

G2_a = nx.Graph([('a', 'b'), ('b', 'h'), ('h', 'g'), ('g', 'a'), ('c', 'd'),
                 ('d', 'f'), ('f', 'e'), ('e', 'c'), ('a', 'd'), ('g', 'f')])
G2_b = nx.Graph([('1', '2'), ('2', '3'), ('3', '4'), ('4', '1'), ('5', '6'),
                 ('6', '7'), ('7', '8'), ('8', '5'), ('1', '5'), ('4', '7')])

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

analyze_isomorphism_builtin(G1_a, G1_b, "QUESTION 1")
analyze_isomorphism_builtin(G2_a, G2_b, "QUESTION 2")
analyze_isomorphism_builtin(G3_a, G3_b, "QUESTION 3A")
analyze_isomorphism_builtin(G3_a, G3_c, "QUESTION 3B")

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
