import networkx as nx
import matplotlib.pyplot as plt
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")
adj_matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

G = nx.Graph()
for i in range(n):
    for j in range(i+1, n):
        if adj_matrix[i][j] == 1:
            G.add_edge(i, j)
print("\nEdges of Original Graph:")
print(list(G.edges()))

L = nx.line_graph(G)
print("\nVertices of Line Graph:")
print(list(L.nodes()))
print("\nEdges of Line Graph:")
print(list(L.edges()))

pos1 = nx.spring_layout(G)
pos2 = nx.spring_layout(L)

plt.figure(figsize=(10,5))
plt.subplot(121)
nx.draw(G,pos1, with_labels=True, node_color='lightblue')
plt.title("Original Graph")
plt.subplot(122)
nx.draw(L,pos2, with_labels=True, node_color='lightgreen')
plt.title("Line Graph (NetworkX)")
plt.show()