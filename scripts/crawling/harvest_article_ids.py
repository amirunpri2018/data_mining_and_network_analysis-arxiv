__author__ = 'Michał Drzał'

import sys
import json
import time
from urllib import request
from bs4 import BeautifulSoup

base_domain = "http://www.arxiv.org"
url_template = base_domain + '/list/{:s}/{:s}?skip={:d}&show={:d}'
throttle_time = 10.0

def get_ids(url):
    html = BeautifulSoup(request.urlopen(url).read().decode('utf-8'))
    content = html.find(id='content').find("dl")

    dts, dds = content.find_all("dt"), content.find_all("dd")

    if len(dts) != len(dds):
        raise Exception("Broken html in: " + url)

    pairs = zip(dts,dds)

    papers = []
    for pair in pairs:
        id = pair[0].span.a["href"].replace("/abs/", "")
        container = pair[1].div.find("div", {"class": "list-authors"})
        links = [a for a in container.find_all("a") if "au:+" in a["href"]]
        authors = [{"id": a["href"].split("au:+")[1].split("/")[0], "fullname":  a.contents[0]} for a in links]
        papers.append({"key":id, "authors":authors})

    return papers


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Please supply input file, field, year and chunk_size")
    else:
        metadata_filename = sys.argv[1]
        field = sys.argv[2]
        year = sys.argv[3]
        chunk_size = int(sys.argv[4])

        with open(metadata_filename, 'r') as metadata_file:
            data = json.load(metadata_file)

        fields = [x for x in data if x["key"] == field]

        if len(fields) == 0:
            raise Exception("No such field")

        counts = [x for x in fields[0]["yearlyCount"] if x["year"] == year]

        if len(counts) == 0:
            raise Exception("No such year")

        count = counts[0]["paperCount"]

        print(field + " " + year + " " + str(count))

        ids = []
        for skip in range(0, count+1, chunk_size):
            url = url_template.format(field, year, skip, chunk_size)
            time.sleep(throttle_time)
            ids.extend(get_ids(url))
            print(url)

        with open(field+"_"+year+".json","w") as output:
            json.dump(ids,output)



