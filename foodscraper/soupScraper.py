#!/usr/bin/python

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

body_tag = soup.body
print body_tag

subNav_tag = soup.find_all('ul')
print len(subNav_tag)
print subNav_tag

print soup.find('subnav')
def has_id_subNav(tag):
	'''
	takes in tag and returns true if 'subNav' is in tag
	'''
	return 'subnav' in tag

print soup.find_all(has_id_subNav)

[x.decompose() for x in soup('script')]
[x.decompose() for x in soup('style')]
##print soup.get_text()

print soup('class = "vert subnav nav1"')


##page1File = open('page1File.txt', 'w')
##page1File.write(str(soup))
##page1File.close()
