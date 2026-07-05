import matplotlib.pyplot as plt
import networkx as nx

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

K5 = nx.complete_graph(5)
pos = nx.spring_layout(K5)
nx.draw(K5, pos, ax=axes[0, 0], with_labels=True)
axes[0, 0].set_title("Complete Graph: K5")

C5 = nx.cycle_graph(5)
pos = nx.spring_layout(C5)
nx.draw(C5, pos, ax=axes[0, 1], with_labels=True)
axes[0, 1].set_title("Cycle Graph: C5")

P5 = nx.path_graph(5)
pos = nx.spring_layout(P5)
nx.draw(P5, pos, ax=axes[1, 0], with_labels=True)
axes[1, 0].set_title("Path Graph: P5")

K23 = nx.complete_bipartite_graph(2, 3)
pos = nx.bipartite_layout(K23, nodes=range(2))
nx.draw(K23, pos, ax=axes[1, 1], with_labels=True)
axes[1, 1].set_title("Bipartite Graph: K2,3")

plt.tight_layout()
plt.show()