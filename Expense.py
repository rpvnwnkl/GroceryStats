class Expense(object):
	def __init__(self, name, cost):
		self._Name = name
		self._Cost = cost

	def Name():
	    doc = "The Name property."
	    def fget(self):
	        return self._Name
	    return locals()
	Name = property(**Name())

	def Cost():
	    doc = "The Cost property."
	    def fget(self):
	        return self._Cost
	    return locals()
	Cost = property(**Cost())

class GroceryItem(Expense):
	def __init__(self, name, cost, amount, measure):
		self._Amount = amount
		self._Measure = measure
		super(GroceryItem, self).__init__(name, cost)

	def Amount():
	    doc = "The Amount property."
	    def fget(self):
	        return self._Amount
	    return locals()
	Amount = property(**Amount())

	def Measure():
	    doc = "The Measure property."
	    def fget(self):
	        return self._Measure
	    return locals()
	Measure = property(**Measure())
