import json, os, re, itertools,sys

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
	pairs = {}
	for filename in filenames:
		print(filename)
		with open(filename) as f:
			chunk = json.load(f)
			for article in chunk:
				authors = [x["id"] for x in article["authors"]]
				for pair in itertools.combinations_with_replacement(authors, 2):
					add_edge(pairs, pair[0], pair[1])

	print("Opened nodes")
	with open("nodes.json") as nodes_file:
		nodes = json.load(nodes_file)

	print("Transforming to dict")
	node_dict = { x: i for i,x in enumerate(nodes) }

	print("Writing")
	with open('edges.csv',"w") as fp:
		for key in pairs:
			line = str(node_dict[key[0]]) + " " + str(node_dict[key[1]]) +" " + str(pairs[key])
			print(line, file = fp )

	with open('edges.json', "w") as f:
		json.dump(edges, f, indent=4)
	