__author__ = 'Michał Drzał'

import json
import os
import os.path
import re
import itertools
import sys

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
	files = os.listdir(sys.argv[1])
	directory = "graphs"
	filenames = filter(lambda x: ("arxiv_" in x) and (".json" in x), files)

	if not os.path.exists(directory):
		os.makedirs(directory)

	for filename in filenames:
		filename = sys.argv[1] + "/" + filename
		chunk = None
		with open(filename) as f:
			chunk = json.load(f)

		# create a list of categories for this year
		categories = set()
		for article in chunk:
			categories.add(article["primary_category"].split(".")[0])


		pairs = {key: {} for key in categories}

		for article in chunk:
			cat = article["primary_category"].split(".")[0]
			authors = [x["id"] for x in article["authors"]]

			#for all pairs of authors
			for pair in itertools.combinations(authors, 2):
				add_edge(pairs[cat], pair[0], pair[1])

		for key in pairs:
			year = "".join([s for s in filename if s.isdigit()])
			output_filename = directory + "/" + key + "_" + year + ".csv"
			with open(output_filename,"w") as fp:
				temp = pairs[key]
				s = [(x[0],x[1], temp[x]) for x in temp]
				print(directory + "/" + key + "_" + year + ".json")
				print(len(s))
				print("author1,author2,common_pubs", file = fp)
				for point in s:
					line = point[0] +"," +point[1] +","+str(point[2])
					print(line, file = fp )
				

		print(categories)