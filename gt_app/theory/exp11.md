Graph coloring is a method of assigning colors to the vertices of a graph such that no two adjacent vertices have the same color.
  Let a graph be represented as:
G = (V, E)
where:
V = set of vertices E = set of edges
A vertex coloring of a graph is a function: C : V → {1,2,3,...,k} such that : C(u) ≠ C(v)	∀ (u,v) ∈ E
This means that if two vertices are connected by an edge, then they must be assigned different colors. The minimum number of colors required to color a graph is called the Chromatic Number of the graph and is denoted by: χ(G)
Hence, χ(G) = min { k : G can be colored using k colors }
Greedy Graph Coloring Algorithm
The Greedy Coloring Algorithm assigns colors to vertices one by one following a specific order. For each vertex, the algorithm assigns the smallest available color that has not been used by its adjacent vertices.

In this method:
The vertex having the highest saturation degree is selected first.
Saturation degree is the number of different colors used by adjacent vertices.
If saturation degrees are equal, the vertex with the highest ordinary degree is selected.

Algorithm
Step 1:Start with all vertices uncolored. Step 2:Select a vertex
Step 3:Assign the smallest possible color that is not used by any adjacent vertex. Step 4:Update the saturation degree of neighboring vertices.
Step 5:Repeat Steps 2 to 4 until all vertices are colored. Step 6:Count the total number of colors used.

For every edge: (u,v) ∈ E
the coloring condition must satisfy: C(u) ≠ C(v)
If the graph is colored using minimum colors, then: χ(G) = Minimum number of colors used
