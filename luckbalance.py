"""
Hackerrank Interview Prep - Greedy Alg - Luck Balance
"""

# Notes:
# input: num - important contests that can be lost
# output: num - maximum amount of luck 
# start @ luck balance = 0
# Each contest (L, T);
# L: lose - balance += luck; win - balance -= luck
# T: importance(1) or not important(0)
# can only lose UP to k. want to lose high luck 

# want to sort list by importance, descending order :o 
# or just make a list of important contests and then sorting that :o
# Complete the luckBalance function below.
def luckBalance(k, contests):
    max_luck_balance = 0
    print('num of important loses', k)
    # contests.sort(key = lambda x: x[1], reverse = True)
    # print(contests)
    important = []
    unimportant = []
    for contest in contests:
        luck, importance = contest
        if importance == 1:
            important.append(contest)
        else:
            unimportant.append(contest)
    # print('important', important)
    # print('unimportant', unimportant)
    
    important.sort(reverse = True)
    # print(important)
    
    i = 1
    while i <= len(important) - k:
        important.pop()
        i += 1
    print(important)

    for contest in important:
        luck, importance = contest
        print('important list')
        print('luck', luck)
        print('importance', importance)
        max_luck_balance += luck
        print(max_luck_balance)
    
    for contest in unimportant:
        luck, importance = contest
        print('unimportant')
        print('luck', luck)
        print('importance', importance)
        max_luck_balance += luck

    return max_luck_balance

# Tests
contest1 = [5 1
2 1
1 1
8 1
10 0
5 0]
k = 3