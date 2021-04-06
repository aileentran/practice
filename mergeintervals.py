"""
Leetcode - 56. Merge Intervals

input: array of intervals [start, end]
output: array of non-overlapping intervals
"""

def merge(intervals):
    return

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

print(merge(intervals1))
print(merge(intervals2))
