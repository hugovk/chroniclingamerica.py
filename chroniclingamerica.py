#!/usr/bin/env python
# encoding: utf-8
"""
API to search Chronicling America

From http://chroniclingamerica.loc.gov/about/api/

    Introduction

    Chronicling America provides access to information about historic
    newspapers and select digitized newspaper pages. To encourage a wide range
    of potential uses, we designed several different views of the data we
    provide, all of which are publicly visible. Each uses common Web protocols,
    and access is not restricted in any way. You do not need to apply for a
    special key to use them. Together they make up an extensive application
    programming interface (API) which you can use to explore all of our data in
    many ways.

    Details about these interfaces are below. In case you want to dive right
    in, though, we use HTML link conventions to advertise the availability of
    these views. If you are a software developer or researcher or anyone else
    who might be interested in programmatic access to the data in Chronicling
    America, we encourage you to look around the site, "view source" often,
    and follow where the different links take you to get started. When
    describing Chronicling America as the source of content, please use the URL
    and a Web site citation, such as "from the Library of Congress, Chronicling
    America: Historic American Newspapers site".

    For more information about the open source Chronicling America software
    please see the LibraryOfCongress/chronam GitHub site. Also, please consider
    subscribing to the ChronAm-Users discussion list if you want to discuss how
    to use or extend the software or data from its APIs.

    The API

    Searching the directory and newspaper pages using OpenSearch

    ...

    Searching newspaper pages is also possible via OpenSearch. This is
    advertised in a LINK header element of the site's HTML template as "NDNP
    Page Search", using this OpenSearch Description document.

    Page search parameters:

     * andtext: the search query
     * format: 'html' (default), or 'json', or 'atom' (optional)
     * page: for paging results (optional)

    Examples:

     * /search/pages/results/?andtext=thomas
       search for "thomas", HTML response
     * /search/pages/results/?andtext=thomas&format=atom
       search for "thomas", Atom response
     * /search/pages/results/?andtext=thomas&format=atom&page=11
       search for "thomas", Atom response, starting at page 11
"""
from __future__ import print_function, unicode_literals
import argparse
import json
import requests

URL_FORMAT = "http://chroniclingamerica.loc.gov/search/pages/results/?%s"


# cmd.exe cannot do Unicode so encode first
def print_it(text):
    print(text.encode('utf-8'))


class ChronAm():
    def __init__(self, search_text, page=1, max_pages=0):
        """Defines the fetcher URL"""
        self.page = page
        self.max_pages = max_pages

        params = []
        params.append("format=json")
        params.append('phrasetext=%s' % search_text)

        self.url = URL_FORMAT % '&'.join(params)
        self.url += '&page=%d'

    def get_total_pages(self):
        """Retrieves the total number of pages for the current operation"""
        r = requests.get(self.url % 1)
        resp = (json.loads(r.text))
        # Floats for rounding up in Py2
        total_items = float(resp['totalItems'])
        items_per_page = float(resp['itemsPerPage'])
        import math
        # Round up
        total_pages = int(math.ceil(total_items / items_per_page))
        if self.max_pages == 0:
            return total_pages
        else:
            return min(self.max_pages, total_pages)

    def get_data(self, page_number):
        """Fetches a page of items from the API"""
        percent = 100.0 * page_number / self.total_pages
        print('Fetching page %i of %i ... %f%%' % (
            page_number, self.total_pages, percent))

        r = requests.get(self.url % page_number)
        resp = (json.loads(r.text))
        if len(resp['items']) > 0:
            return resp['items']
        return []

    def fetch(self):
        """Starts the fetching process"""
        self.total_pages = self.get_total_pages()
        for i in range(self.page, self.total_pages + 1):
            for item in self.get_data(i):
                yield item


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="API to search Chronicling America",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('searchterm', help='Phrase to search for')
    parser.add_argument('-y', '--year', type=int, help='Max year')
    args = parser.parse_args()

    import os
    from pprint import pprint

    args.searchterm = unicode(args.searchterm)

    fetcher = ChronAm(args.searchterm)

    for item in fetcher.fetch():
        year = item['date'][:4]

        if args.year and int(year) > args.year:
            continue

        print("=" * 80)
        # pprint(item.keys())
        # pprint(item)  # Or do something more interesting

        month = item['date'][4:6]
        day = item['date'][6:]
        print(item['date'])
        date = year + "-" + month + "-" + day
        print(date, item['title'], item['place_of_publication'])
        text = item['ocr_eng']
        text = text.replace('\\n', os.linesep)
        print("-" * 80)
        print_it(text)
        print("-" * 80)

        print('http://chroniclingamerica.loc.gov' + item['id'] +
              "#words=" + args.searchterm)


# End of file
