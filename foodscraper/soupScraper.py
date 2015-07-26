#!/usr/bin/python

import re
import urllib
import urlparse
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose

url = 'http://www.hannaford.com/catalog/browse_products.cmd'
soupFile = urllib.urlopen(url, 'r+')
soup = BeautifulSoup(soupFile)
##print(soup.prettify())

title_tag = soup.head.title
print title_tag

##This seems to work, but need to look at actual results to determine difference between techniques
subNav_tag = soup.find_all(id = re.compile('subNav').search('id'))
print subNav_tag
print len(subNav_tag)
##current length is 1522

##This function is a filter to search for id attribute with subNav
##Not quite sure how the return statement works right now, but it does
def has_id_subNav(idattr):
	'''
	takes in tag and returns true if 'subNav' is in tag
	'''
	return idattr and re.compile('subNav').search(idattr)
##This creates a list of the tags with subNav id attributes
subNavId = soup.find_all(id=has_id_subNav)
print subNavId
print 'subNavId Length: '+str(len(subNavId))+' tags'
print 'subNav_tag Length: '+str(len(subNav_tag))+' tags'
print 'needs further analysis'

##length currently 152

##[x.decompose() for x in soup('script')]
##[x.decompose() for x in soup('style')]
##print soup.get_text()

##print soup('class = "vert subnav nav1"')

##print soup.find_all(id=has_id_subNav)

##page1File = open('page1File.txt', 'w')
##page1File.write(str(soup))
##page1File.close()

'''
create tree of nodes
each node is a tag
traverse tree downwards
and across
until the desired div is found
store that div
or act on it in some other fashion
repeat process till end of doc/etc
'''

