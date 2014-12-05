# Basic info

Nodes: 274014

Edges: 4471669

Approx. full diameter: 13 (the longest shortest path between two nodes)

90% effective diameter: 5.175473

# Node degree distribution

![Node degree distribution](node_degree_distribution.png "Node degree distribution")

As we can see node degree distribution indicates a scale-free network

# Counts of components for each size

| Component size | Count         | Component size | Count         |
| -------------- |:-------------:| -------------- |:-------------:|
| 1              | 9512          | 10             | 11            |
| 2              | 2104          | 11             | 11            |
| 3              | 872           | 12             | 4             |
| 4              | 356           | 13             | 2             |
| 5              | 164           | 14             | 2             |
| 6	             | 73            | 15             | 1             |
| 7              | 46            | 16             | 1             |
| 8              | 20            | 17             | 1             |
|                |               | 254106         |	1             |


As we can see we have a plethora of small components and one big component which contains ~93% of all authors.

# More subtle info

Clustering coefficient: 0.566830452965

# Efficiency 
- defined as harmonic mean of all shortest paths between each pair of nodes
- only for largest component, because we can find value for nodes in disconnected components
- such a quantity is an indicator of the traffic capacity of a network
- from Bocaletti, Latora, Moreno, Chavez, Hwang "Complex networks: Structure and dynamics"

Since total number of paths to compute is approximately equal to 32 284 M the computation of the network efficiency is computed on a subsampled set nodes for the largest component. Approximately 10% of nodes where selected randomly and had their shortest paths to all other nodes computed. Inverted sums for selected nodes are available in statistics folder starting with harmonic_means_of_shortest_paths. 






