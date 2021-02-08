"""
Leetcode - 57. Insert Interval

input: list of intervals [num, num], new interval
output: list of non-overlapping intervals in consideration of new interval
"""
def insert(intervals, newInterval):
    if len(intervals) == 0:
        intervals.append(newInterval)
        return intervals

    new_intervals = []
    new_start, new_end = newInterval
    # adding newInterval in list
    for interval in intervals:
        start, end = interval
        if new_start in range(start, end + 1) and new_end > end:
            new_intervals.append([start, new_end])
        elif new_end in range(start, end + 1) and new_start < start:
            new_intervals.append([new_start, end])
        else:
            new_intervals.append(interval)
            new_intervals.append(newInterval)
    # checking all current intervals and keep collapsing them
    new_intervals.sort(key=lambda interval: interval[0])
    result = collapse(new_intervals)
    return result

def collapse(new_intervals):
    for i in range(len(new_intervals) - 1):
        start1, end1 = new_intervals[i]

        for k in range(i + 1, len(new_intervals)):
            if k == len(new_intervals): #hmm... why is k iterating to length of new_intervals
                return new_intervals

            start2, end2 = new_intervals[k]

            if start2 in range(start1, end1 + 1) and end2 > end1:
                new_intervals[i] = [start1, end2]
                new_intervals.pop(i + 1)
                collapse(new_intervals)

            elif end2 in range(start1, end1 + 1) and start2 < start1:
                new_intervals[i] = [start2, end1]
                new_intervals.pop(i + 1)
                collapse(new_intervals)

            elif start2 in range(start1, end1 + 1) and end2 in range(start1, end1 + 1):
                new_intervals.pop(k)
                collapse(new_intervals)

            elif start1 in range(start2, end2 + 1) and end1 in range(start2, end2 + 1):
                new_intervals.pop(i)
                collapse(new_intervals)


    return new_intervals



intervals1 = [[1,3],[6,9]]
newInterval1 = [2,5] #[[1,5],[6,9]]

intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval2 = [4,8] #[[1,2],[3,10],[12,16]]

intervals3 = []
newInterval3 = [5,7] #[[5,7]]

intervals4 = [[1,5]]
newInterval4 = [2,3] #[[1,5]]

intervals5 = [[1,5]]
newInterval5 = [2,7] #[[1,7]]

intervals6 = [[1,5]]
newInterval6 = [6,8] #[[1,5],[6,8]]

intervals7 = [[1,5],[6,8]]
newInterval7 = [0,9] # [[0, 9]]

print(insert(intervals1, newInterval1))
print(insert(intervals2, newInterval2))
print(insert(intervals3, newInterval3))
print(insert(intervals4, newInterval4))
print(insert(intervals5, newInterval5))
print(insert(intervals6, newInterval6))
print(insert(intervals7, newInterval7))
