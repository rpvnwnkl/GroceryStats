#!/usr/bin/python

import re
import urllib
import urlparse
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import copy

def printsoup(soupObj):
	if type(soupObj) == type(soup.a) or type(soupObj) == type(BeautifulSoup()):
  		print 'Soup Length:                ', len(soupObj)
		print 'Number of Soup children:    ', len(list(soupObj.children))
		for xy in soupObj.children:
			try:
				print xy.name
				print xy.string
			except:
				if xy in ['\n']:
					pass
				else:
					print 'printing string: ', xy.string
		print 'Number of Soup Descendants: ', len(list(soupObj.descendants))
		print 'Attributes are:             ', soupObj.attrs
	else:
		print 'Not soup Object'
		print 'Type is ', type(soupObj), 'not ', type(soup.a), ' or ', type(BeautifulSoup())
	return
def printtag(soupTag):
	print type(soupTag)
	print soupTag.name
	print soupTag.string
	print len(soupTag)
	return
url = 'http://www.hannaford.com/catalog/browse_products.cmd'
soupFile = urllib.urlopen(url, 'r+')
soup = BeautifulSoup(soupFile)
printsoup(soup)

soupcopy = copy.copy(soup)

for item in soup(class_='innerWrap'): ##Only works with one innerWrap div on page
	innerWrap = item.extract() ##This pulls out the innerWrap object and renames it 

for item in innerWrap.children:
	if type(item) == type(BeautifulSoup('<!-- -->').string): ##this finds children which are comments
		item.extract() ##this gets rid of them
	else:
		pass
node01 = innerWrap.select('#node01-subNav')
##printsoup(innerWrap)
##printsoup(soup)
printsoup(node01[0])
print node01
for x in node01: ##node01 is a list of the a single ul tag object, the main categories
	printtag(x)
	for xy in x('li'): ##this returns a list of all the li tag objects
		print (xy)
		print type(xy) 
[printsoup(xy) for xy in node01[0]('li')] ##this will do nearly the same as above but return it all in a list
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

