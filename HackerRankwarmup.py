# Complete the sockMerchant function below.

# thoughts
# input: num of socks, array
# output: num of pairs

# sort the array
# make a counter set to 0

# maybe use a while loop? 
# if the current one = next one, increase the counter by 1
# i += 2 to skip to the next thing 

# test case
# n = 100
# ar = [50, 49, 38, 49, 78, 36, 25, 96, 10, 67, 78, 58, 98, 8, 53, 1, 4, 7, 29, 6, 59, 93, 74, 3, 67, 47, 12, 85, 84, 40, 81, 85, 89, 70, 33, 66, 6, 9, 13, 67, 75, 42, 24, 73, 49, 28, 25, 5, 86, 53, 10, 44, 45, 35, 47, 11, 81, 10, 47, 16, 49, 79, 52, 89, 100, 36, 6, 57, 96, 18, 23, 71, 11, 99, 95, 12, 78, 19, 16, 64, 23, 77, 7, 19, 11, 5, 81, 43, 14, 27, 11, 63, 57, 62, 3, 56, 50, 9, 13, 45]

# expected = 28?

def sockMerchant(n, ar):
    ar.sort()
    pairs = 0
    # print(ar)

    i = 0
    while i < len(ar) - 1:
        sock = ar[i]
        nextSock = ar[i + 1]

        # print('sock', sock)
        # print('nextSock', nextSock)
        if sock == nextSock:
            pairs += 1
            # print('pairs', pairs)
            i += 2
        else:
            ar.pop(i)
            # print(ar)
    
    return pairs

# my sol'ns 

# doesn't accout for subsequence steps after alt hits sea level
# def countingValleys(n, s):
#     alt = 0
#     valley = 0

#     print('alt', alt)
#     print('val', valley)

#     for step in s:
#         print('step', step)
#         if step == 'U':
#             alt += 1    
#         else:
#             alt -= 1

#         if alt == 0:
#             valley += 1
#         print('alt', alt)
#         print('val', valley)

#     return valley

# apparently.. counts tiny little dips.. as valleys and.. we didn't want that..?
# def countingValleys(n, s):
#     alt = 0
#     valley = 0
#     # indicate end of hike
#     s = s + '0'

#     i = 0

#     while i < n:
#         print('i', i)
#         step = s[i]
#         nextStep = s[i + 1]
        
#         print('step', step)
#         if step == 'U':
#             alt += 1
#         elif step == 'D':
#             alt -= 1

#         print('alt', alt)
#         print('nextStep', nextStep)
#         if alt == 0 and step != nextStep:
#             valley += 1

#         i += 1

#     return valley
# same result as ^^^^
# def countingValleys(n, s):
#     alt = 0
#     valley = 0

#     print('alt', alt)
#     print('val', valley)

#     for step in s:
#         print('step', step)
#         if step == 'D':
#             alt -= 1
#             if alt == 0:
#                 valley += 1
#         else:
#             alt += 1
#         print('alt', alt)
#         print('val', valley)

#     return valley

# ACTUAL SOL'N
# want to pair alt with upward step to avoid.. tiny dips andd.... going past alt = 0 mark for valleys..?
def countingValleys(n, s):
    alt = 0
    valley = 0

    print('alt', alt)
    print('val', valley)

    for step in s:
        print('step', step)
        if step == 'U':
            alt += 1
            if alt == 0:
                valley += 1
        else:
            alt -= 1
        print('alt', alt)
        print('val', valley)

    return valley


