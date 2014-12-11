__author__ = 'Michał Drzał'

import sys
import json
from lxml import etree
import time
from urllib import request

base_domain = "http://www.arxiv.org"
throttle_time = 10.0

def scrap(id_list):
    url = "http://export.arxiv.org/api/query?id_list=" + ",".join(id_list)

    xml = etree.fromstring(request.urlopen(url).read())

    namespaces = {'ns':'http://www.w3.org/2005/Atom', 'ns-arxiv':"http://arxiv.org/schemas/atom"}

    data = []
    for entry in xml.xpath('//ns:entry',namespaces=namespaces):
        ids = [id.text for id in entry.xpath('ns:id',namespaces=namespaces)]
        published_dates = [published.text for published in entry.xpath('ns:published',namespaces=namespaces)]
        updated_dates = [updated.text for updated in entry.xpath('ns:updated',namespaces=namespaces)]
        titles = [title.text for title in entry.xpath('ns:title',namespaces=namespaces)]
        summaries = [summary.text.replace("\n"," ").strip() for summary in entry.xpath('ns:summary',namespaces=namespaces)]
        dois = [author.text for author in entry.xpath('ns-arxiv:doi',namespaces=namespaces)]
        link_dois = [author.attrib["href"] for author in entry.xpath('ns:link[@title="doi"]',namespaces=namespaces)]
        comments = [author.text for author in entry.xpath('ns-arxiv:comment',namespaces=namespaces)]
        primary_category = [author.attrib["term"] for author in entry.xpath('ns-arxiv:primary_category',namespaces=namespaces)]
        journal_ref = [author.text for author in entry.xpath('ns-arxiv:journal_ref',namespaces=namespaces)]
        categories = [author.attrib["term"] for author in entry.xpath('ns:category',namespaces=namespaces)]

        data.append({
            "id": ids[0].split("abs/")[1].split("v")[0] if len(ids) > 0 else "",
            "published_date": published_dates[0] if len(published_dates) > 0 else "",
            "updated_date": updated_dates[0] if len(updated_dates) > 0 else "",
            "title": titles[0] if len(titles) > 0 else "",
            "abstract": summaries[0] if len(summaries) > 0 else "",
            "doi": dois[0] if len(dois) > 0 else "",
            "link_dois": link_dois[0] if len(link_dois) > 0 else "",
            "comments": comments[0] if len(comments) > 0 else "",
            "primary_category": primary_category[0] if len(primary_category) > 0 else "",
            "journal_ref": journal_ref[0] if len(journal_ref) > 0 else "",
            "categories": categories if len(categories) > 0 else ""
        })

    return data

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please supply input file")
    else:
        pass

    input_filename = sys.argv[1]

    with open(input_filename) as input_file:
        data = json.load(input_file)

    output_data = []
    for chunk in chunks(data, 10):
        keys = [x["key"] for x in chunk]
        print(keys)
        data = scrap(keys)
        time.sleep(throttle_time)
        if len(data) < len(chunk):
            raise Exception("API Query returned fewer data than expected")
        else:
            for pair in zip(data,chunk):
                output_data.append(dict(list(pair[0].items()) + list(pair[1].items())))


    with open(input_filename.replace(".json","_complete.json"), "w") as output:
        json.dump(output_data,output, indent=4)

    print("Finished")