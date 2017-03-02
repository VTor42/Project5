import csv
import re

class Element(object):
	def __init__(self, symbol, element, mass):
		self.symbol = symbol
		self.element = element
		self.mass = mass
def getElementWeight(elementArray, elementSymbol):
	for element in elementArray:
		if elementSymbol == element.symbol:
			return element.mass
def hasNumbers(string):
	return bool(re.search(r'\d', string))

file = open("periodic_table.csv", "rU")
table = csv.reader(file)

elementArray = []
for row in table:
	elementArray.append(Element(row[1], row[2], row[3]))

inputSymbol = raw_input("What is the symbol of the element?\n")
split = inputSymbol.split(" ")
totalMass = 0
for element in split:
	if hasNumbers(element):
		splitSymbol = re.split('(\d+)',element)
		print(splitSymbol)
		totalMass = totalMass + float(getElementWeight(elementArray, splitSymbol[0])) * float(splitSymbol[1])
	else:
		totalMass = totalMass + float(getElementWeight(elementArray, element))
	#print(getElementWeight(elementArray, inputSymbol))

print(totalMass)

file.close()