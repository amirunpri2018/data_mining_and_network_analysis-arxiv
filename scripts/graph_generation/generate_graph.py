__author__ = 'Michał Drzał'

import json, os, re, itertools,sys,os.path

def add_edge(graph, n1, n2):
	if (n1,n2) in graph:
		graph[(n1,n2)] += 1
	elif (n2,n1) in graph:
		graph[(n2,n1)] += 1
	else:
		graph[(n1,n2)] = 1


if len(sys.argv) < 3:
	print("You need to specify folder with metadata nodes.json file and out file")
else:
	input_folder = sys.argv[1]
	nodes_file = sys.argv[2]
	output_file = sys.argv[3]

	with open(nodes_file) as f:
		node_dict = json.load(f)

	filenames = [input_folder + "/" + x for x in os.listdir(sys.argv[1]) if x.startswith("arxiv_") and x.endswith(".json")]

	pairs = {}
	print("Retrieving edges")
	for filename in filenames:
		print(filename)
		with open(filename) as f:
			chunk = json.load(f)
			for article in chunk:
				authors = [x["id"] for x in article["authors"]]
				for pair in itertools.combinations_with_replacement(authors, 2):
					add_edge(pairs, pair[0], pair[1])


	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	print("Saving edges to file: " + output_file )
	with open(output_file ,"w") as fp:
		for key in pairs:
			line = str(node_dict[key[0]]) + " " + str(node_dict[key[1]]) +" " + str(pairs[key])
			print(line, file = fp )
