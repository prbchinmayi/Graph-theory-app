import matplotlib.pyplot as plt
import networkx as nx

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

K_5 = nx.Graph()
K_5.add_nodes_from(range(5))
K_5.add_edges_from([(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)])
pos=nx.spring_layout(K_5)
nx.draw(K_5,pos, ax=axes[0,0], with_labels=True)
axes[0,0].set_title("complete graph: K5")

C_5 = nx.Graph()
C_5.add_nodes_from(range(5))
C_5.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,0)])
pos=nx.spring_layout(C_5)
nx.draw(C_5,pos, ax=axes[0,1], with_labels=True)
axes[0,1].set_title("circle graph: C5")

P_5 = nx.Graph()
P_5.add_nodes_from(range(5))
P_5.add_edges_from([(0,1),(1,2),(2,3),(3,4)])
pos=nx.spring_layout(P_5)
nx.draw(P_5,pos, ax=axes[1,0], with_labels=True)
axes[1,0].set_title("path graph: P5")

K_2_3 = nx.Graph()
K_2_3.add_nodes_from(range(5))
K_2_3.add_edges_from([(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)])
pos={}
pos[0]=(1,1)
pos[1]=(2,1)
pos[2]=(0,0)
pos[3]=(1,0)
pos[4]=(2,0)
nx.draw(K_2_3,pos, ax=axes[1,1],with_labels=True)
axes[1,1].set_title("bipartite graph: K2,3")
plt.show()
