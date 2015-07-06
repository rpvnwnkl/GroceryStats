#!/usr/bin/env python
from assembler import *
import time
import csv
from matplotlib import pyplot
import numpy

''' reads and re-interprets time sample '''
steve = time.strptime("30Nov2000", "%d%b%Y")
print ''.join(str([steve[2], steve[1], steve[0]]))
newSteve = time.strftime('%d%b%Y', steve)
print newSteve

fileName='./foodList_x.csv'

def readfile(fileName):
    with open(fileName, 'rb') as csvfile:
        print 'opened '+fileName
        foodList = csv.DictReader(csvfile, delimiter = ',', quotechar = '"')
        tmpList = []
        for row in foodList:
            tmpList.append(row)
            ##print row
    for item in tmpList:
        if '/' in item['Date']:
            if len(item['Date'].split('/')[0]) == 1:
##                print 'fired'
                item['Date']=''.join(('0', item['Date']))
            item['Date'] = time.strftime('%d%b%Y', time.strptime(item['Date'],'%m/%d/%Y'))
        if item['Category'] == '':
            print 'no Category on '+item
    return tmpList


'''creates food object from spreadsheet file'''
tmpFood = readfile(fileName)
food = Groceries(tmpFood)
'''save to new file to reflect changes in values''' 
food.save('foodList_x_test.csv')


'''three name changes to fix seller info in original document'''
##food.changeName('Hannafords', 'Hannaford', 'Seller')
##food.changeName('Uncle Deans', "Uncle Dean's", 'Seller')
##food.changeName('Trader Joes', "Trader Joe's", 'Seller')

'''prints out list of unique sellers'''
##for item in food.sellerList():
##    print item
'''
def straightPlot():
    dateArray = []
    costArray = []
    unsortedFood = []
    wDayArray = {}
    yDayArray = {}
    for item in food.getFood():
##        unsortedFood += (item.pDate()[7], item.itemCost())
        pyplot.figure(1)
        x, y = float(item.getDict()['Date'][7]), float(item.getDict()['Cost'])
        z = item.wDay()
        yd = item.yDay()
        pyplot.plot(x, y, '-ro')
        dateArray.append(x)
        costArray.append(y)
        if z in wDayArray.keys():
            wDayArray[z].append(y)
        else:
            wDayArray[z] = [y]
        if yd in yDayArray.keys():
            yDayArray[yd] += y
        else:
            yDayArray[yd] = y
           
##    sortedFood = sorted(unsortedFood, x[0])
    
    for x in wDayArray:
        wDayArray[x] = sum(wDayArray[x])
    pyplot.figure(5)
    for (k, v) in sorted(yDayArray.items()):
        pyplot.bar(k, v)
##    pyplot.figure(2)
##    sortedX = [x[0] for x in sortedFood]
##    sortedY = [y[1] for y in sortedFood]
##    coefficients = numpy.polyfit(sortedX, sortedY, 3)
##    polynomial = numpy.poly1d(coefficients)
##    ys = polynomial(dateArray)
##    pyplot.plot(dateArray, ys, '-ro')
    pyplot.title('Year Day versus Cost')
    
    pyplot.figure(4)
    for x in wDayArray.keys():
        pyplot.bar(x, wDayArray[x])
    pyplot.title('Weekday versus average Cost')
    
    pyplot.figure(3)
    pyplot.hist(costArray, len(dateArray))
    pyplot.title('frequency of daily purchase amounts')
    pyplot.show()
    '''
class Stats(object):
    
    def monthlyTotal(self, beg=1, end=12):
        '''returns dict of monthly totals and list of months'''
        firstMonth = time.strftime("%B", time.strptime(str(beg), "%m"))
        print firstMonth
        print beg
        lastMonth = time.strftime("%B", time.strptime(str(end), "%m"))
        print lastMonth
        print end
        monthTotals = {}
        for item in food.getFood():
            tmpMonth = item.yMonth()
##            print tmpMonth
            if tmpMonth in range(beg, end+1):
##                print True
                if tmpMonth in monthTotals.keys():
##                    print 'adding '+str(item.itemCost())+' to total'
                    monthTotals[tmpMonth] += item.itemCost()
                else:
                    monthTotals[tmpMonth] = item.itemCost()
        print monthTotals
        
        for key in sorted(monthTotals.keys()):
            print time.strftime("%b", time.strptime(str(key), "%m"))+': $'+str(monthTotals[key])
        return monthTotals
     
facts = Stats()
print facts.monthlyTotal(1, 6)

def monthlyGroup():
    months = {}
    for item in food.getFood():
        tmpMonth = item.yMonth()
        if tmpMonth in months.keys():
            months[tmpMonth].append(item)
        else:
            months[tmpMonth] = [item]
    return months
##tmp = monthlyGroup()
##for x in tmp.keys():
##    for y in tmp[x]:
##        print str(x)+': '+y.getName()
    
##saveIt('foodList_a.csv')
