Data mining stage
=================

Data source description
-----------------------

The arXiv (pronounced "archive", as if the "X" were the Greek letter Chi, χ) is a repository of electronic preprints, known as e-prints, of scientific papers in the fields of mathematics, physics, astronomy, computer science, quantitative biology, statistics, and quantitative finance, which can be accessed online. In many fields of mathematics and physics, almost all scientific papers are self-archived on the arXiv.

Each field has an abbreviation assigned e.g . 

- astrophysics : astro-ph
- mathematics : math
- computer science : cs
- quantitative biology : q-bio
- quantitative finance : q-fin
- statistics : stat

Iterating over all articles
---------------------------

Users can view article listings for each year under list route. Results are paged, thus to cycle through all articles two number parameters are passed in query string to specify which page we need.

http://arxiv.org/list/{field_abbreviation}/{last_two_digits_of_year}?skip={number_of_articles}&show={number_of_articles}

Example: http://arxiv.org/list/math/00?skip=50&show=25 (show articles for Mathematics and year 2000 from 50 to 75)

It is helpful to know beforehand how many articles for given field and year are there. Script [generate_yearly_paper_counts.py](../generate_yearly_paper_counts.py) does precisely that and dumps the results into a json file.

Having that knowledge under belt we can generate set of links that we need to crawl in order to gather the data we need.

Extracting articles identificators
----------------------------------

Using generated previously links we can can extract from each page useful information about article. We can extract its id and ids of its authors along with their full names. Unfortunately listings don't show any info about the abstracts. For that we'll crawle arXiv API.

In each page articles are contained inside __dl__ tag. With pairs of __dt__ and __dd__ tags. First link __dt__ has id embedded in it href in form: abs/{id}. There are at least two ID types on arXiv (and they're not interchangeable): 

- YYMM.NNNN (e.g. 1411.0027 leads to astrophysics paper from 2014 October)
- {field_name}/YYMM201 (e.g. math/9601201 leads to mathematics paper from 1996 January)

Article ids can have version appended in form: "v" + number

From each article we can also extract paper authors or more importantly their ids, since we can't get them through API.

They're inside __dd__ tags inside __div__ with class="list-authors". Inside link tags full names are embedded and in href attribute exits id in form: {garbage}au:+{author_id}/{garbage}.

Script [harvest_article_ids.py](../harvest_article_ids.py) extracts both article and author id, author fullname pairs and stores them in json file. It required field name, year and file produced by [generate_yearly_paper_counts.py](../generate_yearly_paper_counts.py) to know how many link are there to crawl.

Getting rest of the article data
--------------------------------

arXiv has an API that allows to download info about specific articles given that we have their ids. Data is returned as an nicely-formatted XML. API URL: http://export.arxiv.org/api/query?id_list={comma_separated_list_of_ids}. We can provide up to 10 ids in one request. Returned XML is in form:

```xml
<entry>
    <id>http://arxiv.org/abs/{article id}</id>
    <updated>{date}</updated>
    <published>{date}</published>
    <title>{article title}</title>
    <summary>{Summary text}</summary>
    <author>
      <name>{author name}</name>
    </author>
    <arxiv:comment>{comment text}</arxiv:comment>
    <arxiv:journal_ref>{journal reference}</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/{article id}" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/{article id}" type="application/pdf"/>
    <arxiv:primary_category term="{category abbr.}">
    <category term="{category abbr.}"/>
    <category term="{category abbr.}"/>
    <category term="{category abbr.}"/>
  </entry>
```

Data from xml is then merged with data from http crawling and form the final dataset.

Data mining stage results
=========================

Dataset contains zipped [article metadata for each year](https://drive.google.com/folderview?id=0B8yQRmV2S-ZLcS1oQXM0bzYxU1k&usp=sharing). 

Constructed graphs
-----------------

Dataset contains also  extracted graph data:
- [nodes.json](https://drive.google.com/file/d/0B8yQRmV2S-ZLT1pvSzJ3YUpOd0U/view?usp=sharing) contain a list of all authours in the arXiv up to 2013 represented as dictionary: author string id and corresponding integer id, ~200k authors
- [total.zip](https://drive.google.com/file/d/0B8yQRmV2S-ZLTUc0cWNmem1ocmM/view?usp=sharing) contains a list of edges between authors from nodes.json, edge is created when two authors write a paper together (with weight 1) and its weight is incremented with each next publication (nodes.zip + edges.zip create a full coauthorship graph for arXiv up to 2013)
- [grouped.zip](https://drive.google.com/file/d/0B8yQRmV2S-ZLeHhNRVVEekk0VXM/view?usp=sharing) contains a four graphs for time periods: 1991-1999, 2000-2004, 2005-2009, 2010-2013
- [single.zip](https://drive.google.com/file/d/0B8yQRmV2S-ZLNGJObFJPWlItVmM/view?usp=sharing) contains graphs for each year
- [yearly field graphs](https://drive.google.com/folderview?id=0B8yQRmV2S-ZLREh4ZUtKc1llblE&usp=sharing) coauthorship graphs for each field and year in json

[Created dataset](https://drive.google.com/folderview?id=0B8yQRmV2S-ZLQTVENmhycHVTM00&usp=sharing)

