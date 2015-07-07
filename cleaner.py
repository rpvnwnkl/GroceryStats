#!/usr/bin/env python
from assembler import *
##import time
##import csv
from matplotlib import pyplot
import numpy

##''' reads and re-interprets time sample '''
##steve = time.strptime("30Nov2000", "%d%b%Y")
##print ''.join(str([steve[2], steve[1], steve[0]]))
##newSteve = time.strftime('%d%b%Y', steve)
##print newSteve

fileName='./foodList_x_test.csv'

'''creates food object from spreadsheet file'''
tmpFood = readfile(fileName)
food = Groceries(tmpFood)
'''save to new file to reflect changes in values'''
food.save('foodList_x1_test.csv')


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
    def __init__(self, selfObject):
        self.Queue = selfObject

    def monthlyTotal(self, beg=1, end=12):
        '''returns dict of monthly totals'''
        firstMonth = time.strftime("%B", time.strptime(str(beg), "%m"))
        lastMonth = time.strftime("%B", time.strptime(str(end), "%m"))
        monthTotals = {}
        for item in self.Queue:
            tmpMonth = item.Month()
            if tmpMonth in range(beg, end+1):
                if tmpMonth in monthTotals.keys():
                    monthTotals[tmpMonth] += item.itemCost()
                else:
                    monthTotals[tmpMonth] = item.itemCost()
                    
        monthlyAVG = numpy.mean([monthTotals[x] for x in monthTotals])
        print 'Monthly average purchase amount from {} through {} is: {}'.format( firstMonth, lastMonth, str(monthlyAVG))
        
        print 'Monthly totals for months '+firstMonth+' through '+lastMonth+'.'
        for key in sorted(monthTotals.keys()):
            print time.strftime("%b", time.strptime(str(key), "%m"))+': $'+str(monthTotals[key])
        print '\n'
        return monthTotals
    
    def typeTotals(self, beg, end):
        '''returns dict of category totals per month'''
         
        firstMonth = time.strftime("%B", time.strptime(str(beg), "%m"))
        lastMonth = time.strftime("%B", time.strptime(str(end), "%m"))
        allMonths = {}
        for item in self.Queue:
            itemVal = item.getRowDict()
            itemType = itemVal['Type']
            itemCost = float(itemVal['Cost'])
            tmpMonth = item.Month()
            if tmpMonth in range(beg, end+1):##check if in desired range
                if tmpMonth in allMonths.keys(): ##check if month already in dict
                    if itemType in allMonths[tmpMonth]:##check if type is in month dict
                        allMonths[tmpMonth][itemType] += itemCost ##add cost to type value in month dict
                    else:
                        allMonths[tmpMonth][itemType] = itemCost ##if not add it as origin value
                else:                    
                    allMonths[tmpMonth] = {itemType: itemCost} ##add month and add initial dict value
                    
##        print 'Category totals for each month '+firstMonth+' through '+lastMonth+'.'
##        for key in sorted(allMonths):
##            print time.strftime("%b", time.strptime(str(key), "%m"))+':'
##            for itemtype in sorted(allMonths[key]):
##                print itemtype+': $'+str(allMonths[key][itemtype])
##            print '\n'
        print 'Category totals for each month '+firstMonth+' through '+lastMonth+'.'

        '''converting dict to list of lists'''
        allInList = []
        for key in sorted(allMonths):
            monthList = []
            for item in allMonths[key]:
                monthList.append((item, allMonths[key][item]))
            '''orders tuples by value size'''
            allInList.append(sorted(monthList, key=lambda cost: cost[1], reverse=True))
            
        '''proceeds through and prints the list month by month'''
        currentMonth = beg
        for month in allInList:
            print time.strftime("%b", time.strptime(str(currentMonth), "%m"))+':'
            currentMonth += 1
            for catVal in month:
                print catVal[0]+': $'+str(catVal[1])
            print '\n'
            
        return allInList
facts = Stats(food)
facts.monthlyTotal(1, 6)
facts.typeTotals(1, 6)
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
