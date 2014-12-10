# Analysis of subgraphs

Coauthorship was divided into batches based on publication date of articles into four time periods:

1991 - 1999 - batch1

2000 - 2004 - batch2

2005 - 2010 - batch3

2011 - 2013 - batch4


## Community detection

We assumed that with each year amount of coauthored roughly doubles. This allows us to filter out authors that occasionally written together and put a lower constraint on minimum edge weight to be considered.

batch1 - 0.5 paper/year, minimum common publications : 4

batch2 - 1 paper/year, minimum common pulications  : 5

batch3 - 2 papers/year, minimum common pulications  : 10

batch4 - 4 papers/year, minimum common pulications  : 16


For finding communities we used [cfinder](http://www.cfinder.org/), which uses [clique percolation method](http://en.wikipedia.org/wiki/Clique_percolation_method). We set up a limit per node calculation to 2 seconds. Results:

batch1 - 492 cliques, no approximation was needed

batch2 -  3713 cliques, no approximation was needed

batch3 - number of exact cliques=2086, number of approx. cliques=75

batch4 - number of exact cliques=1867, number of approx. cliques=315

Generated communites are available [here](https://drive.google.com/folderview?id=0B8yQRmV2S-ZLTWw0czJ5MUxMQ28&usp=sharing).

##  Betweenness centrality

Betweenness centrality was computed for each author in each batch was computed. Due to limited computing power centrality for each node was computed on a 1% of all other nodes. Computed with [Snap.py](http://snap.stanford.edu/snappy/) library [GetBetweennessCentr](http://snap.stanford.edu/snappy/doc/reference/GetBetweennessCentr.html) procedure.

Results available in [betweenness directory]().


