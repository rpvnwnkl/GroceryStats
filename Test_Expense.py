import unittest
from Expense import *

class Test(unittest.TestCase):
	def test_init(self):
		name = "ItemName"
		cost = 1.25
		amount = 5
		measure = 'ounces'
		myGroceryItem = GroceryItem(name, cost, amount, measure)
		assert myGroceryItem.Name == name
		assert myGroceryItem.Cost == cost
		assert myGroceryItem.Amount == amount
		assert myGroceryItem.Measure == measure

if __name__ == '__main__':
    # When this module is executed from the command-line, run all its tests
    unittest.main()
