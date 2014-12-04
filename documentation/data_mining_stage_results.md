Data mining stage results
=========================

Dataset contains zipped article metadata for each year. 

Constructed graphs
-----------------

Dataset contains also three zip archives with extracted graph data:
- [nodes.zip](https://drive.google.com/file/d/0B8yQRmV2S-ZLekM5OVB4QWVwaE0/view?usp=sharing) contain a list of all authours in the arXiv up to 2013 represented as two element list: author id and full name, nodes of the graph, ~200k authors
- [edges.zip](https://drive.google.com/file/d/0B8yQRmV2S-ZLaUlmdG1Nc053bk0/view?usp=sharing) contains a list of edges between authors from nodes.zip, edge is created when two authors write a paper together (with weight 1) and its weight is incremented with each next publication (nodes.zip + edges.zip create a full coauthorship graph for arXiv up to 2013), ~4000k edges
- [graphs.zip](https://drive.google.com/file/d/0B8yQRmV2S-ZLOTQwbHkzellvc1k/view?usp=sharing) coauthorship graphs for each field and year in json

[Created dataset](https://drive.google.com/folderview?id=0B8yQRmV2S-ZLQTVENmhycHVTM00&usp=sharing)



