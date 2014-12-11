__author__ = 'Michał Drzał'

import json, os, re, itertools,sys,os.path

def add_edge(graph, n1, n2):
	if (n1,n2) in graph:
		graph[(n1,n2)] += 1
	elif (n2,n1) in graph:
		graph[(n2,n1)] += 1
	else:
		graph[(n1,n2)] = 1


if len(sys.argv) < 3 or not (os.path.exists(sys.argv[1] and os.path.exists(sys.argv[2])  ):
	print("You need to specify a valid folder with graphs")
else:
	source_folder = sys.argv[1]
	dest_file = sys.argv[2]
	filenames = [source_folder + "/" + x for x in os.listdir(source_folder) if x.startswith("arxiv_") and x.endswith(".json")]
	auths = set()

	print("Retrieving nodes")
	for filename in filenames:
		print(filename)
		with open(filename) as f:
			chunk = json.load(f)
			for article in chunk:
				authors = [x["id"] for x in article["authors"]]

				for author in authors:
					auths.add(author)
				
	auths = list(auths)
	node_dict = { x: i for i,x in enumerate(auths) }

	print("Saving nodes mapping to file: " + dest_file)
	with open(dest_file, "w") as ofile:
		json.dump(node_dict, ofile, indent=4)

	
