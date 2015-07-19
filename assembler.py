import time
import csv
import os
from recordFood.dataInput import * 

class Groceries(object):

    def __init__(self):
        ''' given a foodList Dict this creates food objects using Item class and collects them in a list '''
	tmpFood = readfile()
	self.foodObjects = list((Item(row) for row in tmpFood if row['Category'] == 'Grocery'))
    def getFood(self):
        ''' returns list of food Item objects '''
        return self.foodObjects
    def getFoodDicts(self):
        return self.foodDicts
    def __str__(self):
        ''' identifies itself as a list of food Item dicts, relies on Item str methods for clarity '''
        ret_str = ""
        for item in self.foodObjects:
                ret_str += "".join(str(item))
        return ret_str
    def __repr__(self):
        return self.foodObjects
    def __iter__(self):
        return iter(self.foodObjects)
    def changeName(self, oldName, newName, category):
        ''' given the category, the existing name str, and the
            desired name str, will go through foodObject list and change as necessary '''
        for item in self.getFood():
            if item.sameName(oldName, category):
                item.nameChange(newName, category)
                print oldName+"-->"+newName
        for item in self.getFood():
            if item.sameName(oldName, category):
                print 'found one not fixed'

    def sellerList(self):
        '''searches through list of food Item objects and
            pulls unique 'Seller' names and returns them in a list'''
        tmpList = []
        for item in self.foodObjects:
            if item.getSeller() not in tmpList:
                tmpList.append(item.getSeller())
        tmpList.sort()
        return tmpList

    def getDates(self):
        return self.Dates
    
    def save(self, fileName):
        '''saves object as a csv file named as filename.
            filename can be any type but will be read as type string'''
        fileName = str(fileName) 
        with open(fileName, 'w') as csvfile:
            fieldnames = ['Name', 'Amount', 'Measure', 'Cost', 'Seller', 'Date', 'Buyer', 'Category', 'Type']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for item in self.getFood():
                writer.writerow(item.getRowDict())
##        print 'foodObject saved as '+fileName+'!'
    

##A class is created for food items, which are denoted by each row of the food dictionary
class Item(Groceries):
    def __init__(self, row): ##init local food dict
        self.rowDict = row ##saves the dict format
        self.cats = list(self.rowDict.keys())##categories are just the dict keys
##	should be:
##		self.Name
##		self.Amount
##		self.Measure
##		self.Cost
##		self.Seller
##		self.Date
##		self.Buyer
##		self.Category
##		self.Type
        for x in row.keys():
            setattr(self, x, row[x])
    def Date(self):
        return time.strptime(self.Date, "%d%b%Y")
    def Month(self):
        return int(time.strftime('%m', time.strptime(self.Date, "%d%b%Y")))
    def itemCost(self):
        return float(self.Cost)
    def getName(self):
        return self.Name
    def getRowDict(self):
        return self.rowDict
    def getSeller(self):
        return self.Seller
            
    def __str__(self): ##returns item as a Dict
        return str(self.rowDict)
    def __repr__(self):##returns food item object as key, value pairs
        return self.rowDict.items()
    def __iter__(self):
        return iter(self.rowDict)

    def getCats(self): ##returns list of keys as food categories
        return self.cats

    def nameChange(self, newName, category): ##changes value of given key in food dict
        self.rowDict[category] = newName    
        self.Category = newName

    def sameName(self, oldName, category): ##check to see if name is the same
        return self.rowDict[category] == oldName

def foodPlot():
    pass
def saveIt(fileName, foodObject):
    '''writes food object to file, fileName should be str'''
    fileName = str(fileName) 
    with open(fileName, 'w') as csvfile:
        fieldnames = ['Name', 'Amount', 'Measure', 'Cost', 'Seller', 'Date', 'Buyer', 'Category', 'Type']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for item in foodObject.getFood():
            writer.writerow(item.getDict())
