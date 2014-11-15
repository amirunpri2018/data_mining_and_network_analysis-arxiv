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

Users can view article listings for each year under:

http://arxiv.org/list/{field_abbreviation}/{last_two_digits_of_year} 

(example http://arxiv.org/list/math/00)

Results are paged. To cycle through all articles two additional parameters passed in query string are required: skip, show.

http://arxiv.org/list/{field_abbreviation}/{last_two_digits_of_year}?skip={number_of_articles}&show={number_of_articles}

(exampleh http://arxiv.org/list/math/00?skip=50&show=25)


