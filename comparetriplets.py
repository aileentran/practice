"""
HackerRank - Compare the triplets

input: two arrays of nums - Alice and Bill
output: 1 array of nums [Alice's score, Bill's score]

compare Alice and Bill's score at each index.
+1 score if one score is > than other
return an array w/ Alice's score then Bill's
"""

def compareTriplets(a, b):
    score = [0, 0]

    for i in range(0, len(a)):
        a_score = a[i]
        b_score = b[i]
        if a_score > b_score:
            score[0] += 1
        elif b_score > a_score:
            score[1] += 1
    return score

a1 = [1, 2, 3]
b1 = [3, 2, 1]
print(compareTriplets(a1, b1)) #[1, 1]

a2 = [5, 6, 7]
b2 = [3, 6, 10]
print(compareTriplets(a2, b2)) #[1, 1]

a3 = [17, 28, 30]
b3 = [99, 16, 8]
print(compareTriplets(a3, b3)) #[2, 1]
