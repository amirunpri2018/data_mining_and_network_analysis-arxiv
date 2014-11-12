__author__ = 'Michał Drzał'

import sys
import time
import json
from urllib import request
from bs4 import BeautifulSoup
from datetime import date

base_domain = "http://www.arxiv.org"


def get_fields_abbreviations():
    text = request.urlopen(base_domain).read().decode('utf-8')
    html = BeautifulSoup(text)

    condition = lambda a: len(a.contents) > 0 and a.contents[0] == "recent"
    links = filter(condition,  html.find_all("a"))

    return [{"name": a.parent.a.contents[0], "key": a['href'].replace("/recent", "").replace("/list/","")} for a in links]


def field_start_year(key):
    # artificial link, page contains info when first data is available
    url = base_domain + '/list/{:s}/0000'.format(key)
    html = BeautifulSoup(request.urlopen(url).read().decode('utf-8'))
    # first link in content and its content
    return int(html.find(id='content').a.contents[0][0:2])


# creates range of years for given field
# more precisely: their last two digits in a form of string
def year_range(year):
    current_year = date.today().year
    year += 1900 if year > (current_year % 100) else 2000
    return [str(x)[2:] for x in range(year,current_year+1)]


def get_paper_count(key, year):
    url = base_domain + '/list/{:s}/{:s}'.format(key, year)
    soup = BeautifulSoup(request.urlopen(url).read().decode('utf-8'))
    pagination_element = soup.find(id='dlpage').small

    page_urls = pagination_element.find_all("a")
    visible_page = pagination_element.find_all("b")[-1]

    # if there are no urls in this dom element
    # meaning we have only one page and it is current one
    text = visible_page if len(page_urls) == 0 else page_urls[-1]
    tokens = text.contents[0].split("-")

    return int(tokens[0]) if len(text) < 2 else int(tokens[1])


if __name__ == "__main__":
    print(get_fields_abbreviations())
    if len(sys.argv) < 2:
        print("Please supply output file")
    else:
        output_filename = sys.argv[1]
        abbreviations = get_fields_abbreviations()

        metadata = []

        for pair in abbreviations:
            key, name, start_year = pair["key"], pair["name"], field_start_year(pair["key"])
            print(name)

            yearly_count = []

            for year in year_range(start_year):
                time.sleep(2.5)
                print(year)
                count = get_paper_count(key, year)
                yearly_count.append({"year": year, "paperCount": count})

            yearly_count.append({"key": key, "name": name, "yearlyCount": yearly_count})


        with open(output_filename,"w") as output_file:
            json.dump(metadata, output_file)



