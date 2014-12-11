from __future__ import print_function
from collections import Counter
import sys
__author__ = 'Michal Drzal'

import snap,json


# requires python 2.7 and 64-bit machine
G1 = snap.TUNGraph.New()

nodes = []

with open(sys.argv[1] + "/data/edges.csv") as f:
	for line in f:
		tokens = line.split()
		n1, n2, weight = int(tokens[0]), int(tokens[1]), int(tokens[2])
		if not G1.IsNode(n1):
			nodes.append(G1.AddNode(n1))
		if not G1.IsNode(n2):
			nodes.append(G1.AddNode(n2))

		G1.AddEdge(n1, n2)

#with open("data/largest_connected_component.csv","w") as f:
#	MxScc = snap.GetMxScc(G1)
#	for EI in MxScc.Edges():
#	    print("%d %d" % (EI.GetSrcNId(), EI.GetDstNId()),file=f)

print("starting")
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
MxScc = snap.GetMxScc(G1)
snap.GetBetweennessCentr(MxScc, Nodes, Edges, 0.05)
with open(sys.argv[1] + "/data/centralities.csv","w") as f:
	for node in Nodes:
	    print( "%d %f" % (node, Nodes[node]), file= f)
print("ending")

# print("started")
## eigen vector centrality
#NIdEigenH = snap.TIntFltH()
#snap.GetEigenVectorCentr(G1, NIdEigenH)

#with open("statistics/nodes_EigenVector.csv","w") as f:
#	for item in NIdEigenH:
#		print(str(item) + " " + str(NIdEigenH[item]), file=f)
#print("done")

##code to get clustering coefficient
#print(snap.GetClustCf(G1))


## code to get strongly connected components
#Components = snap.TCnComV()
#snap.GetSccs(G1, Components)

#cnt = Counter([CnCom.Len() for CnCom in Components])

#print(cnt.most_common())

#with open("statistics/component_size_distribution.csv","w") as f:
#	for item in cnt.most_common():
#		print(str(item[0]) + " " + str(item[1]), file=f)

# #code to generate node degree distribution
#DegToCntV = snap.TIntPrV()
#snap.GetDegCnt(G1, DegToCntV)


#degrees =[]
#counts = []

#with open("statistics/node_degree_distribution.csv","w") as f:
#	for item in DegToCntV:
#		degrees.append(float(item.GetVal1()))
#		counts.append(float(item.GetVal2()))
#		print(str(item.GetVal1()) + " " + str(item.GetVal2()), file=f)