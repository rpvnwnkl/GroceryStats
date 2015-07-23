#!/usr/bin/python

import re
import urllib
import urlparse
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import copy

def printsoup(soupObj):
	if type(soupObj) == type(soup.a) or type(soupObj) == type(BeautifulSoup()):
  		print 'Soup Length: ', len(soupObj)
		print 'Number of Soup children: ', len(list(soupObj.children))
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
		print 'Attributes are: ', soupObj.attrs
	else:
		print 'Not soup Object'
		print 'Type is ', type(soupObj), 'not ', type(soup.a), ' or ', type(BeautifulSoup())
	return

url = 'http://www.hannaford.com/catalog/browse_products.cmd'
soupFile = urllib.urlopen(url, 'r+')
soup = BeautifulSoup(soupFile)
printsoup(soup)

soupcopy = copy.copy(soup)

subNav_tag = soup.find_all(id = re.compile('subNav')) ##this finds all tags under subNav ids

for item in soup(class_='innerWrap'): ##Only works with one innerWrap div on page
	newSoup = item.extract() ##This pulls out the innerWrap object and renames it 

for item in newSoup.children:
	if type(item) == type(BeautifulSoup('<!-- -->').string): ##this finds tags which are comments
		item.extract() ##this gets rid of them
	else:
		pass
subNode_tree = {}
for tag in subNav_tag:
     tmpId = tag.get('id')
     tmpId = tmpId.split('-')
     subNode_tree[tag] = [child for child in tag.children if child not in ['\n']]

##print subNode_tree[subNav_tag[0]]

total = 0
for x in subNode_tree:
        total += len(x.a)
       ## print x.a
       ## print x.get('id')
        for y in x.children:
		if y != '\n':
			pass##	print y.string

print total

printsoup(newSoup)
printsoup(soup)
printsoup(soupcopy)

##for x in subNode_tree:
##        print type(x)
##        for tag in x.children:
##                print x
print 'see'
i = 0
for tag in soup.select('ul li'):
        if tag.get('id')==re.compile('subnode'):
                print tag
                print'\n'
                i += 1
print i
##This function is a filter to search for id attribute with subNav
##Not quite sure how the return statement works right now, but it does
def has_id_subNav(idattr):
	'''
	takes in tag and returns true if 'subNav' is in tag
	'''
	return idattr and re.compile('subNav').search(idattr)
##This creates a list of the tags with subNav id attributes
subNavId = soup.find_all(id=has_id_subNav)
##print subNavId
print 'subNavId Length: '+str(len(subNavId))+' tags'
print 'subNav_tag Length: '+str(len(subNav_tag))+' tags'
print 'needs further analysis'

##length currently 152
##now it's 151

##for tag in subNav_tag.descendants:
##	if tag.get('li'):
##		print tag.get('a')

##for parent in soup.a.parents:
##	if parent is None:
##		print parent
##	else:
##		print parent.name
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

