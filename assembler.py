import time
import csv
##def readfile(fileName):
##    with open(fileName, 'rb') as csvfile:
##        print 'opened '+fileName
##        foodList = csv.DictReader(csvfile, delimiter = ',', quotechar = '"')
##        tmpList = []
##        for row in foodList:
##            tmpList.append(row)
##            print row
##    return tmpList
    
##this object holds all the food 'Item' objects
class Groceries(object):

    def __init__(self, foodList):
        ''' given a foodList Dict this creates food objects using Item class and collects them in a list '''
        self.foodObjects = list((Item(row) for row in foodList if row['Category'] == 'Grocery'))
        self.Dates = []
        self.Dates.append(item.pDate() for item in self.foodObjects if item.pDate() not in self.Dates)
        print 'foodObjects made'
        
    def getFood(self):
        ''' returns list of food Item objects '''
        return self.foodObjects

    def __str__(self):
        ''' identifies itself as a list of food Item dicts, relies on Item str methods for clarity '''
        ret_str = ""
        for item in self.foodObjects:
                ret_str += "".join(str(item))
        return ret_str

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
        print 'foodObject saved as '+fileName+'!'
    

##A class is created for food items, which are denoted by each row of the food dictionary
class Item(Groceries):
    def __init__(self, row): ##init local food dict
        self.rowDict = row ##saves the dict format
        self.cats = self.rowDict.keys()##categories are just the dict keys
##        print self.rowDict['Date']
##        self.rowDict['Date'] = time.strptime(self.rowDict['Date'], "%d%b%Y")
    def pDate(self):
        return self.rowDict['Date']
    def yDay(self):
        return self.pDate()[7]
    def wDay(self):
        return self.pDate()[6]
    def yMonth(self):
        return self.pDate()[1]
    def itemCost(self):
        return float(self.rowDict['Cost'])
    def getName(self):
        return self.rowDict['Name']
    def getRowDict(self):
        return self.rowDict
    def getSeller(self):
        return self.rowDict['Seller']
            
    def __str__(self): ##returns item as a Dict
        return str(self.rowDict.items())
    def __repr__(self):##returns food item object as key, value pairs
        return self.rowDict

    def getCats(self): ##returns list of keys as food categories
        return self.cats

    def nameChange(self, newName, category): ##changes value of given key in food dict
        self.rowDict[category] = newName    
        
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
