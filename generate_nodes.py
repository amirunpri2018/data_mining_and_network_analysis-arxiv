import json, os, re, itertools


filenames = [x for x in os.listdir() if x.startswith("arxiv_") and x.endswith(".json")]

auths = set()
print(filenames)
for filename in filenames:
	with open(filename) as f:
		chunk = json.load(f)
		for article in chunk:
			print(article["key"])
			authors = [x["id"] for x in article["authors"]]
			for author in authors:
				auths.add(author)
			


ofile  = open('nodes.json', "w")
json.dump(list(auths), ofile, indent=4)
ofile.close()