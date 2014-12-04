import json
import os
import re
import itertools
import sys

if len(sys.argv) < 2:
	print("You need to specify folder with graphs")
else:
	files = os.listdir(sys.argv[1])
	filenames = filter(lambda x: ("arxiv_" in x) and (".json" in x), files)

	for filename in filenames:
		chunk = None
		with open(filename) as f:
			chunk = json.load(f)
			categories = set()
			for article in chunk:
				categories.add(article["primary_category"].split(".")[0])

			pairs = {key: {} for key in categories}
			for article in chunk:
				cat = article["primary_category"].split(".")[0]
				authors = [x["id"] for x in article["authors"]]
				for pair in itertools.combinations(authors, 2):
					if pair in pairs[cat]:
						pairs[cat][pair] += 1
					elif (pair[1], pair[0]) in pairs[cat]:
						pairs[cat][(pair[1], pair[0])] += 1
					else:
						pairs[cat][pair] = 1

			for key in pairs:
				year = filename.replace("arxiv_","").replace(".json","")
				with open("graphs/" + key + "_" + year + ".csv","w") as fp:
					temp = pairs[key]
					s = [(x[0],x[1], temp[x]) for x in temp]
					print("graphs/" + key + "_" + year + ".json")
					print(len(s))
					print("author1,author2,common_pubs", file = fp)
					for point in s:
						print(point[0] +"," +point[1] +","+str(point[2]), file = fp )
					

			print(categories)

		


