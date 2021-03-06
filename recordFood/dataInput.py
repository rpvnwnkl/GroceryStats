#!/usr/bin/env python   
import os
import time
import csv

def readfile():
    tmpList = []
    for root, dirs, files in os.walk('./foodFiles/'):
        for name in files:
            with open(os.path.join(root, name), 'rb') as csvfile:
                foodList = csv.DictReader(csvfile, delimiter = ',', quotechar = '"')
                for row in foodList:
                    tmpList.append(row)
    for item in tmpList:
        item = fixDate(item)
    return tmpList

def fixDate(item):
    ''' takes in item, returns item with formatted date field '''
    if '/' in item['Date']:
        if len(item['Date'].split('/')[0]) == 1: ##this checks to see if month is single digit
            item['Date']=''.join(('0', item['Date'])) ##if so, it adds a zero to help with the parsing
        item['Date'] = time.strftime('%d%b%Y', time.strptime(item['Date'],'%m/%d/%Y'))
    return item     


