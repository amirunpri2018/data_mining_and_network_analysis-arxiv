import json, os, re, itertools


filenames = [x for x in os.listdir() if x.startswith("arxiv_") and x.endswith(".json")]

pairs = {}
print(filenames)
for filename in filenames:
	with open(filename) as f:
		chunk = json.load(f)
		for article in chunk:
			print(article["key"])
			authors = [x["id"] for x in article["authors"]]
			for pair in itertools.combinations_with_replacement(authors, 2):
				if pair in pairs:
					pairs[pair] += 1
				elif (pair[1], pair[0]) in pairs:
					pairs[(pair[1], pair[0])] += 1
				else:
					pairs[pair] = 1

edges = [(key[0], key[1],pairs[key]) for key in pairs]


ofile  = open('edges.json', "w")
json.dump(edges, ofile, indent=4)
ofile.close()


