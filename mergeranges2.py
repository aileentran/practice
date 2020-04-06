# revisiting merging meetings on Interview Cake!

# thoughts
# function called merge_ranges()
# input: list of multiple ranges
# output: list of condensed ranges

# meetings might NOT be in order - > order them first 
# range is EXCLUSIVE! 

# order the meetings
# soo! make an empty list to return 
# have a current meeting time frame? set it to the first val of ORDERED list

# loop through the ORDERED list
# if the current item == current meeting or the curr item end is within the range of curr meeting-> continue to next item
# if start of curr item is within the range (AND the end of curr item is past the range?)
# set the current time frame end range to curr item end range
# else
# append curr time range into list
# set the curr item as curr time range 

# ?? need to append the very last time range?? 

# outside of loop
# return the list

# bleh woah! not working! 

def merge_ranges(times):
	"""Condense ranges."""

	# ordered times
	times.sort()

	merged = []
	curr_meeting = times[0]
	curr_start = curr_meeting[0]
	curr_end = curr_meeting[1]

	for time in times:
		start = time[0]
		end = time[1]

		if time == curr_meeting or end in range(curr_start, curr_end + 1):
			continue
		elif start in range(curr_start, curr_end + 1):
			curr_end = end
		else:
			merged.append(curr_meeting)
			curr_meeting = time

	return merged
