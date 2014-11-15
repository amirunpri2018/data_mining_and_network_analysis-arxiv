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

From each article we can also extract paper authors or more importantly their ids, since we can't get them through API.

They're inside __dd__ tags inside __div__ with class="list-authors". Inside link tags full names are embedded and in href attribute exits id in form: {garbage}au:+{author_id}/{garbage}.

Script [harvest_article_ids.py](../harvest_article_ids.py) extracts both article and author id, author fullname pairs and stores them in json file. It required field name, year and file produced by [generate_yearly_paper_counts.py](../generate_yearly_paper_counts.py) to know how many link are there to crawl.

Getting rest of the article data
--------------------------------

arXiv has an API that allows to download info about specific articles given that we have their ids. Data is returned as an nicely-formatted XML. API URL: http://export.arxiv.org/api/query?id_list={comma_separated_list_of_ids}. We can provide up to 10 ids in one request. Returned XML is in form:

<entry>
    <id>http://arxiv.org/abs/cs/9901002v1</id>
    <updated>1999-01-10T03:21:23Z</updated>
    <published>1999-01-10T03:21:23Z</published>
    <title>KnightCap: A chess program that learns by combining TD(lambda) with
  game-tree search</title>
    <summary>  In this paper we present TDLeaf(lambda), a variation on the TD(lambda)
algorithm that enables it to be used in conjunction with game-tree search. We
present some experiments in which our chess program ``KnightCap'' used
TDLeaf(lambda) to learn its evaluation function while playing on the Free
Internet Chess Server (FICS, fics.onenet.net). The main success we report is
that KnightCap improved from a 1650 rating to a 2150 rating in just 308 games
and 3 days of play. As a reference, a rating of 1650 corresponds to about level
B human play (on a scale from E (1000) to A (1800)), while 2150 is human master
level. We discuss some of the reasons for this success, principle among them
being the use of on-line, rather than self-play.
</summary>
    <author>
      <name>Jonathan Baxter</name>
    </author>
    <author>
      <name>Andrew Tridgell</name>
    </author>
    <author>
      <name>Lex Weaver</name>
    </author>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">9 pages</arxiv:comment>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">MACHINE LEARNING Proceedings of the Fifteenth International
  Conference (ICML '98), ISBN 1-55860-556-8, ISSN 1049-1910, Madison WISCONSIN,
  July 24-27 1998, pages 28-36</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/cs/9901002v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/cs/9901002v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cs.LG" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.LG" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.AI" scheme="http://arxiv.org/schemas/atom"/>
    <category term="I.2.6" scheme="http://arxiv.org/schemas/atom"/>
  </entry>

