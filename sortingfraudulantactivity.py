"""Hackerrank Interview Prep - Sorting"""

# Notes
# input: expenditures - list of expenses, d = time frame
# output: num = number of notifications
# expense on any day >= 2x median -> send notice
# first d timeframe = data gathering = 0 notifications
# median = odd list - middle number; even list - average 2 middle values
# even list -> num1 + num2 / 2 BUT multiply by 2 for notification so.. just add ?
# median = arranging nums from lowest to highest

# empty median variable (not necessary?)
# empty comparison variable 
# empty notification variable

# loop through list (nested?)
# first time frame from range(0, d) = only median
# then afterwards, loop through the days one by one
# find median: in timeframe, sort ascending
# odd length: (len - 1) // 2 + 1 ; 
# even : num1 ((len - 1) // 2) + num2 ((len - 1) // 2 + 1) -> COMPARISON
# create comparison = median x 2
# look at the next day after time frame
# see if >= comparison, yes = notification += 1, no = continue\

# outside loop, return notification

# Error - some test cases; does not run within limits

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    comparison = 0
    notifications = 0

    for idx in range(len(expenditure) - d):
        timeframe = expenditure[idx: d + idx]
        print(timeframe)
        timeframe.sort()
        check_exp = expenditure[d + idx]

        print('check_exp', check_exp)
        if d % 2 != 0:
            idx1 = (d - 1) // 2 
            comparison = timeframe[idx1] * 2
        else:
            idx1 = (d - 1) // 2
            idx2 = idx1 + 1
            comparison = timeframe[idx1] +timeframe[idx2]
        
        print('comparison', comparison)
        if check_exp >= comparison:
            notifications += 1
    
    return notifications