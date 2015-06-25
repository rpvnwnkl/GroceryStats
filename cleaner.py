import csv

fileName='foodList_1.csv'
def readfile(fileName):
    with open(fileName, 'rb') as csvfile:
        foodList = csv.DictReader(csvfile, delimiter = ',', quotechar = '"')
        tmpList = []
        for row in foodList:
            tmpList.append(row)
    return tmpList
            
def nameChange(oldName, newName, category, food):
    food.changeName(category, oldName, newName)
    

class Groceries(object):
    def __init__(self, foodList):
        ##creates food object list and puts the Item objects inside row by row
        self.foodObjects = list((Item(row) for row in foodList))
    def getFood(self):
        return self.foodObjects
    def __str__(self):
        return self.foodObjects
    def changeName(self, category, oldName, newName):
        for item in self.getFood():
            if item.sameName(oldName, category):
                item.nameChange(newName, category)
                print oldName+'-->'+newName
        for item in self.getFood():
            if item.sameName(oldName, category):
                print 'found one not fixed'
    def sellerList(self):
        ##searches through dict and pulls names and adds to a list
        tmpList = []
        for item in self.foodObjects:
            if item.getSeller() not in tmpList:
                tmpList.append(item.getSeller())
        tmpList.sort()
        return tmpList

    
##A class is created for food items, which are denoted by each row of the food dictionary
class Item(Groceries):
    def __init__(self, row): ##init local food dict
        self.rowDict = row ##saves the dic format
        self.cats = self.rowDict.keys()
    def getDict(self):
        return self.rowDict
    def getSeller(self):
        return self.rowDict['Seller']
            
    def __str__(self): ##returns item as a Dict
        return str(self.rowDict.items())
    def __repr__(self):##returns item as key, value pairs
        return self.rowDict

    def getCats(self): ##returns list of keys as food categories
        return self.cats

    def nameChange(self, newName, category): ##changes value of given key in food dict
        self.rowDict[category] = newName
        
    def sameName(self, oldName, category): ##check to see if name is the same
        return self.rowDict[category] == oldName
    
food = Groceries(readfile(fileName))    
nameChange('Hannafords', 'Hannaford', 'Seller', food)
nameChange('Uncle Deans', "Uncle Dean's", 'Seller', food)
nameChange('Trader Joes', "Trader Joe's", 'Seller', food)

for item in food.sellerList():
    print item

with open('foodList_x.csv', 'w') as csvfile:
    fieldnames = ['Name', 'Amount', 'Measure', 'Cost', 'Seller', 'Date', 'Buyer', 'Category', 'Type']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for item in food.getFood():
        writer.writerow(item.getDict())
