##Need:
Script which pulls info from Hannaford website, creating a tree of descending categories with food products on the bottom

##How:
* Iteratively load html pages from hannaford.com
* Search page for descriptive tags/keywords indicating relevant information
* Save information in tree format (preserving parent and children nodes)
* Ensure text is formatted and data is structured properly

##First Steps:
* Write function to load html page
* Add methods to find keywords in page
* Add methods to find and add relevant links to a queue
* Create object structure to store information
* Store information on page in object structure (tree)
* Add new and relevant links to queue
* Move on to next link in queue

I think it will probably be best to search the website using _depth first_ methods

###Function to load html page:

####Probably can use the following libraries:

__*Latest update is to use Beautiful Soup library as start*__

urlparse and urljoin to extract and then execute urls in the page:
* https://docs.python.org/2/library/urlparse.html#module-urlparse
* https://docs.python.org/2/library/urlparse.html#urlparse.urljoin

urllib.urlopen() to open urls as file objects:
* https://docs.python.org/2/library/urllib.html#urllib.urlopen
Python 3 version is also compatible with Python 2.7:
* https://docs.python.org/2/library/urllib2.html#urllib2.urlopen

Possibly might be preferable to use urllib.urlretreive() as it can save to file:
* https://docs.python.org/2/library/urllib.html#urllib.urlretrieve

HTMLParser to read through html tags, etc:
* https://docs.python.org/2/library/htmlparser.html#examples

readline might be useful:
* https://docs.python.org/2/library/readline.html


Not for this, but maybe for the food items, use SQLite:
* https://docs.python.org/2/library/sqlite3.html
and
* https://docs.python.org/2/library/dbm.html

Shelve and pickle are potential database/dict tools, but need further evaluation to see if they will be useful
* https://docs.python.org/2/library/shelve.html
* https://docs.python.org/2/library/pickle.html

Might be worth looking over linecache if a db seems like overkill:
* https://docs.python.org/2/library/linecache.html
or
* https://docs.python.org/2/library/tempfile.html

