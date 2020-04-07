# revisiting merging meetings on Interview Cake!

# input: list of time ranges
# output: list of condensed time ranges
# times are NOT always in order
# sol'n should work without upper bound :o 

# thoughts
# sort the time ranges with .sort()
# make an empty list for condensed time ranges
# variable to store current time range = ACCOUNT FOR EXCLUSION OF END! 
# start and stop variables?

# loop through times
# start and stop variables?

# if.. the time range is within the current range 
# and if end of range is past the range 
# extend the end range to this end + 1 (account for exclusion)
# no need to account for starts before range bc.. already sorted stuff

# if the start time is after range
# append the current range tuple thingy into the results list 

# outside of loop(?), append the last thingy mabob into the list
# return the list of condensed ranges

def merge_ranges(times):
	"""Condense ranges."""

	times.sort()
	# print(times)

	merged = []
	# set to very first meeting
	curr_start = times[0][0]
	curr_end = times[0][1]
	# print('curr_start', curr_start)
	# print('curr_end', curr_end)

	for time in times:
		start = time[0]
		end = time[1]
		# print('start', start)
		# print('end', end)

		if start == curr_start and end == curr_end:
			continue
		elif start in range(curr_start, curr_end + 1) and end > curr_end:
			curr_end = end
			# print('curr_start', curr_start)
			# print('curr_end', curr_end)
		else:
			merged.append((curr_start, curr_end))
			curr_start = start
			curr_end = end

	# account for very last time frame still hanging out
	merged.append((curr_start, curr_end))

	return merged
