chroniclingamerica.py
=====================

## Python API to search Chronicling America newspaper pages.

### Usage

```python
from chroniclingamerica import ChronAm
from pprint import pprint

fetcher = ChronAm(search_term)
for item in fetcher.fetch():
    pprint(item)  # Or do something more interesting
```

Calling `fetch()` returns a generator of articles in JSON format. Articles are retrieved one [results] page at a time. 
To get the total number of pages available, use `get_total_pages()`.

`pprint(item)` gives something like this:

```python
{u'alt_title': [u'Combined New York morning newspapers',
                u'Combined New York Sunday newspapers',
                u'New York daily tribune',
                u'New York tribune',
                u'New-York daily tribune'],
 u'batch': u'batch_dlc_denmark_ver01',
 u'city': [u'New York'],
 u'country': u'New York',
 u'county': [u'New York'],
 u'date': u'19100102',
 u'edition': None,
 u'edition_label': u'',
 u'end_year': 1924,
 u'frequency': u'Daily',
 u'id': u'/lccn/sn83030214/1910-01-02/ed-1/seq-17/',
 u'language': [u'English'],
 u'lccn': u'sn83030214',
 u'note': [u'Archived issues are available in digital format as part of the Library of Congress Chronicling America online collection.',
           u'Available on microfilm from University Microfilms International, and Recordak.',
           u'Evening ed.: Evening edition of the tribune, 1866.',
           u'Merged with: New York herald (New York, N.Y. : 1920); to form: New York herald, New York tribune.',
           u'Semiweekly ed.: New-York tribune (New York, N.Y. : 1866 : Semiweekly), 1866-<1899>.',
           u'Triweekly eds.: New-York tri-weekly tribune, <1900>-1903, and: New York tribune (New York, N.Y. : 1903), 1903-<1909>.',
           u'Weekly ed.: New-York tribune (New York, N.Y. : 1866 : Weekly), 1866-<1906>.'],
 u'ocr_eng': u'PART 18,\nPROW OF UNCLE SAM\'S "CONCRETE BATTLESHIP," SO CALLED, AND TYPE OF\nTHE MIGHTY WEAPONS SHE WILL CARRY.\nDrawing shows one end of the elliptical fort with thick walls of concrete, now being erected on the little island of El Fraile, in Manila Bay. Bslow is a gun of the 14-inch style, and for pur\nposes of comparison a body of twenty-one mounted troopers is placed in juxtaposition. The fort will carry two of these 14-inch guns, each 53^2 feet long. For additional details see article\ninside.\nSUNDAY. JANUARY 2, 1910.\nEIGHT PAGES.',
 u'page': u'',
 u'place': [u'New York--New York--New York'],
 u'place_of_publication': u'New York [N.Y.]',
 u'publisher': u'New York Tribune',
 u'section_label': u'',
 u'sequence': 17,
 u'start_year': 1866,
 u'state': [u'New York'],
 u'subject': [u'New York (N.Y.)--Newspapers.',
              u'New York (State)--New York County.--fast--(OCoLC)fst01234953',
              u'New York (State)--New York.--fast--(OCoLC)fst01204333',
              u'New York County (N.Y.)--Newspapers.'],
 u'title': u'New-York tribune.',
 u'title_normal': u'new-york tribune.',
 u'type': u'page',
 u'url': u'https://chroniclingamerica.loc.gov/lccn/sn83030214/1910-01-02/ed-1/seq-17.json'}
 ```

The [JSON given by `url`](https://chroniclingamerica.loc.gov/lccn/sn83030214/1910-01-02/ed-1/seq-17.json) contains links to a [JP2 image](https://chroniclingamerica.loc.gov/lccn/sn83030214/1910-01-02/ed-1/seq-17.jp2) and [PDF](https://chroniclingamerica.loc.gov/lccn/sn83030214/1910-01-02/ed-1/seq-17.pdf) of the page, as well as [OCR text](https://chroniclingamerica.loc.gov/lccn/sn83030214/1910-01-02/ed-1/seq-17/ocr.txt) and [OCR metadata](https://chroniclingamerica.loc.gov/lccn/sn83030214/1910-01-02/ed-1/seq-17/ocr.xml).

### Parameters

Currently there's only one parameter.

* `search_term`
  * The search query

### To Do

More search parameters.

### Origin

Thanks to [@zeroviscosity](https://github.com/zeroviscosity/) for the
[Article fetcher for The Guardian newspaper's Open Platform API](https://github.com/zeroviscosity/guardian-article-fetcher),
which this project is based on, and to 
[The Library of Congress](https://www.loc.gov/) for [Chronicling America](https://chroniclingamerica.loc.gov/) and their 
[API](https://chroniclingamerica.loc.gov/about/api/).
