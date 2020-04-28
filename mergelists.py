"""
input: two lists of ints -> both ordered already
output: one ordered list of ints

thoughts

loop through first list
append each item into second list

outside loop
sort(list2)

return list2

TEST CASES
input:
my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

output:[1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
"""

# def merge_lists(my_list, alices_list):

#     # Combine the sorted lists into one large sorted list

#     for order in my_list:
#     	alices_list.append(order)

#     alices_list.sort()

#     return alices_list

# OR

# def merge_lists(my_list, alices_list):

# 	return sorted(my_list + alices_list)

# ORRR! 

# lists are already in order so.. trying to make it faster
"""
edge cases: 
One or both of our input lists is 0 elements or 1 element
One of our input lists is longer than the other.
One of our lists runs out of elements before we're done merging.
"""
def merge_lists(my_list, alices_list):

	# Combine the sorted lists into one large sorted list

	longer = max(my_list, alices_list)
	combined = []

	i = 0

	while i < len(longer):
		smaller = min(my_list[i], alices_list[i])
		larger = max(my_list[i], alices_list[i])
		combined.append(smaller)
		combined.append(larger)

		i += 1

	return combined

