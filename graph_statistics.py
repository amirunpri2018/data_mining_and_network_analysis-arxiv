__author__ = 'Michal Drzal'

import snap

# requires python 2.7 and 64-bit machine
G1 = snap.TUNGraph.New()

with open("data/edges.csv") as f:
	for line in f:
		tokens = line.split()
		n1, n2, weight = int(tokens[0]), int(tokens[1]), int(tokens[2])
		if not G1.IsNode(n1):
			G1.AddNode(n1)
		if not G1.IsNode(n2):
			G1.AddNode(n2)

		G1.AddEdge(n1, n2)

print "Stats"
snap.PrintInfo(G1, "arXiv netwrok", "stats.txt", False)


