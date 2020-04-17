# convert dictionary to ONE DIMENSIONAL list and ONE DIMENSIONAL list back to dictionary
# input: dictionary
# output: list





# input: list
# output: dictionary 



"""
Test case

dictionary:
fruits = {
	'citrus': ['limes', 'cuties'],
	'berries': ['cherries', 'blueberries', 'strawberries'],
	'three': 3
}

list:
fruits = ['citrus', 'limes', 'cuties', 'berries', 'cherries', 'blueberries', 'strawberries', 'three', 3]


"""


def dicttolist(dict):
	"""Converting a dictionary into a list!"""

	alist = []

	for fruit in fruits:
		alist.append(fruit)
		alist.append(fruits[fruit])

	return alist

def listtodict(alist):
	"""Converting list into a dictionary!"""

	adict = {}

	i = 0

	while i <= len(alist) - 1:
		key = alist[i]
		val = alist[i + 1]
		adict[key] = val

		i += 2

	return adict