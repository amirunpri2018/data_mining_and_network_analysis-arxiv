Data mining stage results
=========================

Dataset contains zipped article metadata for each year. Dataset contains also two files representing nodes and edges for co-authorship. Both are json files. 
- nodes.json contain a list of two element lists. First element is id of author and second is fullname.
- edges.json contain a list of three element lists. First and second elements are author ids from node.json and third is weight corresponding to number of coauthored papers (nodes can be connected to themselves, weights on those edges correspond to number of articles published by author)

nodes.json contains about 200k authors, edges.json contains around 4000k edges

[Created dataset](https://drive.google.com/folderview?id=0B8yQRmV2S-ZLQTVENmhycHVTM00&usp=sharing)



