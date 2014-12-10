__author__ = 'Michał Drzał'

import json, os, re, itertools,sys,os.path

def add_edge(graph, n1, n2):
	if (n1,n2) in graph:
		graph[(n1,n2)] += 1
	elif (n2,n1) in graph:
		graph[(n2,n1)] += 1
	else:
		graph[(n1,n2)] = 1


if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
	print("You need to specify a valid folder with graphs")
else:
	filenames = [sys.argv[1] + "/" + x for x in os.listdir(sys.argv[1]) if x.startswith("arxiv_") and x.endswith(".json")]
	auths = set()
	pairs = {}
	print("Retrieving nodes and edges")
	for filename in filenames:
		print(filename)
		with open(filename) as f:
			chunk = json.load(f)
			for article in chunk:
				authors = [x["id"] for x in article["authors"]]

				for author in authors:
					auths.add(author)

				for pair in itertools.combinations_with_replacement(authors, 2):
					add_edge(pairs, pair[0], pair[1])
				
	auths = list(auths)

	target_dir = sys.argv[1] + "/data"
	if not os.path.exists(target_dir):
		os.makedirs(target_dir)

	print("Saving nodes to file")
	with open(target_dir + '/nodes.json', "w") as ofile:
		json.dump(auths, ofile, indent=4)

	node_dict = { x: i for i,x in enumerate(auths) }
	auths = None

	print("Saving edges to file")
	with open(target_dir + '/edges.csv',"w") as fp:
		for key in pairs:
			line = str(node_dict[key[0]]) + " " + str(node_dict[key[1]]) +" " + str(pairs[key])
			print(line, file = fp )
