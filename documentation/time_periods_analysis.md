# Analysis of subgraphs

Coauthorship was divided into batches based on publication date of articles into four time periods:

1991 - 1999

2000 - 2004

2005 - 2010

2011 - 2013


## Community analysis

We assumed that with each year amount of coauthored roughly doubles. This allows us to filter out authors that occasionally written together and put a lower constraint on minimum edge weight to be considered.

1991 - 1999 - 0.5 paper/year, minimum common publications : 4

2000 - 2004 - 1 paper/year, minimum common pulications  : 5

2005 - 2010 - 2 papers/year, minimum common pulications  : 10

2011 - 2013 - 4 papers/year, minimum common pulications  : 16


For finding communities we used [cfinder](http://www.cfinder.org/), which uses [clique percolation method](http://en.wikipedia.org/wiki/Clique_percolation_method). We set up a limit per node calculation to 2 seconds. Results:

1991 - 1999 - 492 cliques, no approximation was needed

2000 - 2004 -  3713 cliques, no approximation was needed

2005 - 2010 - number of exact cliques=2086, number of approx. cliques=75

2011 - 2013 - number of exact cliques=1867, number of approx. cliques=315

