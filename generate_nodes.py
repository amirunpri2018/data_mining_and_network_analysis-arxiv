import json, os, re, itertools,sys

if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
	print("You need to specify a valid folder with graphs")
else:
	filenames = [sys.argv[1] + "/" + x for x in os.listdir(sys.argv[1]) if x.startswith("arxiv_") and x.endswith(".json")]

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
				


	with open('nodes.json', "w") as ofile:
		json.dump(list(auths), ofile, indent=4)