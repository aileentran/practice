"""
Leetcode - 56. Merge Intervals

input: array of intervals [start, end]
output: array of non-overlapping intervals

Thoughts
new intervals might overlap with other intervals in list
maybe infinite loop until the length of new list == old list == no new merges?

sort the intervals in ascending order based on starts
create a copy of prev intervals

infinite loop through intervals, looking at 2 at a time
start1, end1 and start2, end2.
if start2 within the range of start1 and end1, pick max end times
append start1, max end into empty list

OR recursion?
when there is a merge, recursively call this with the new list of intervals..?
what is the base case..


Let's start with the most basic one merge

New approach
sort
empty results list
loop through intervals and compare current with last val in results list
if it overlaps, merge them
if not, add the current interval into the list
should also account for multiple overlaps
"""

def merge(intervals):
    intervals.sort()
    merged = []

    for interval in intervals:
        start, end = interval
        if merged == [] or merged[-1][1] < start:
            merged.append(interval)
        else:
            prevStart, prevEnd = merged[-1]
            merged[-1] = [prevStart, max(prevEnd, end)]

    return merged

intervals1 = [[1,3],[2,6],[8,10],[15,18]]
"""
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6]
"""

intervals2 = [[1,4],[4,5]]
"""
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

intervals3 = [[1,4],[0,2],[3,5]]
# output: [[0, 5]]

intervals4 = [[1, 3]]

print(merge(intervals1))
print(merge(intervals2))
print(merge(intervals3))
# print(merge(intervals4))
