chroniclingamerica.py
=====================

## Python API to search Chronicling America newspaper pages.

### Usage

```python
from chroniclingamerica import ArticleFetcher
from pprint import pprint

fetcher = ChronAm(search_term)
for item in fetcher.fetch():
    # pprint(item)  # Or do something more interesting
```

Calling `fetch()` returns a generator of articles in JSON format. Articles are retrieved one [results] page at a time. 
To get the total number of pages available, use `get_total_pages()`.

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
[The Library of Congress](http://www.loc.gov/) for [Chronicling America](http://chroniclingamerica.loc.gov/) and their 
[API](http://chroniclingamerica.loc.gov/about/api/).
