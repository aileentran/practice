# convert dictionary to list and list back to dictionary
# input: dictionary
# output: list

# make empty list

# loop through dictionary
# append key and value into the list


# return list




# input: list
# output: dictionary 
# even nums are keys
# odd nums are values!! 
# oh oh! maybe look at two values at a time?????? two pointerrrsss??

# make an empty dictionary

# while loopin through the list EVEN NUMBERSS??
# make the current item the key and the next item the value?!
# BOOM!

# return the dictionary


"""
Test case

dictionary:
fruits = {
	'citrus': ['limes', 'cuties'],
	'berries': ['cherries', 'blueberries', 'strawberries'],
	'three': 3
}

list:
fruits = ['citrus', ['limes', 'cuties'], 'berries', ['cherries', 'blueberries', 'strawberries'], 'three', 3]



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