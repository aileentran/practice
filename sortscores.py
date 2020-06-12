# input: list of unsorted scores, highest score
# output: list of sorted scores
# want it in less than O(n log n) runtime 

def sort_scores(unsorted_scores, highest_possible_score):

    # Sort the scores in O(n) time
    score_counts = [0] * (highest_possible_score+1)

    # Populate score_counts AND MARK SCORE LOCATION?
    for score in unsorted_scores:
        score_counts[score] += 1

    print(score_counts)

print(sort_scores([37, 89, 41, 65, 91, 53], 100))