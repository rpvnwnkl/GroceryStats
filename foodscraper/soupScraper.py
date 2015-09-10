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

def getNode(nodeObj):
    try:
        ##print node
        if 'id' in nodeObj.attrs:
            tempID = nodeObj.attrs['id']
            print tempID
            return tempID.split('-')
        else:
            return
    except:
        return
def inNodeDict(idString, nodeDict, subNodeDict):
    if len(idString) == 0:
        return nodeDict
    elif idString[0] in subNodeDict:
        subKey = idString[0]
        idString.pop(0)
        nodeDict[subKey] = inNodedict(idString, nodeDict, subNodeDict[subKey])
    else:
        subNodeDict[idString[0]] = {idString[0]:{}}
        return subNodeDict

##url = 'http://www.hannaford.com/catalog/browse_products.cmd'
##soupFile = urllib.urlopen(url, 'r+')
soupFile = open('page1File.txt', 'r')
soup = BeautifulSoup(soupFile)
##printsoup(soup)

soupcopy = copy.copy(soup)

for item in soup(class_='innerWrap'): ##Only works with one innerWrap div on page
	innerWrap = item.extract() ##This pulls out the innerWrap object and renames it, unfortunately is saved as list?
        print type(innerWrap)

for item in innerWrap.children:
	if type(item) == type(BeautifulSoup('<!-- -->').string): ##this finds children which are comments
            item.extract() ##this gets rid of them
	else:
		pass
node01 = innerWrap.select('#node01-subNav')
##printsoup(innerWrap)
##printsoup(soup)
##printsoup(node01[0])
##print node01
def clickNode(node, nodeDict = {}):
    ##print type(node)
    ##print len(node)
    try:
        printtag(node)
        idList = getNode(node)
        ##print node.attrs
        if idList:
            print inNodeDict(idList, nodeDict, nodeDict)

            for x in range(len(idList)):
                print x
                
                if idList[0] in nodeDict:
                    if node.string:
                        nodeDict[idList[x]].append(node.string)
                else:
                    if node.string:
                        nodeDict[idList[x]] = [node.string]
        for x in node:

            print len(nodeDict)
            clickNode(x, nodeDict)

    except:
        return nodeDict
    '''if type(node) != type(list):
        idList = getNode(node)
        print idList
        if idList:
            
            for x in node: ##node01 is a list of the a single ul tag object, the main categories
##	        printtag(x)

                return clickNode(x, nodeDict)
        ##print node
                ##for xy in x('li'): ##this returns a list of all the li tag objects
		  ##  print (xy)
		    ##print type(xy)
     '''               ##print getNode(xy)
    return nodeDict

##print clickNode(node01)
##print clickNode(soup
print clickNode(innerWrap)
##[printsoup(xy) for xy in node01[0]('li')] ##this will do nearly the same as above but return it all in a list
##page1File = open('page1File.txt', 'w')
##page1File.write(str(soup))
##page1File.close()
soupFile.close()

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

