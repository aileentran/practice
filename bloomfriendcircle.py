"""
Leetcode mock

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
 

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

 

Constraints:

1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]

Prev
2 / 2
"""



# Notes
# input: 2d array
# output: int - number of friend circles
# friend circle = direct and indirect relationships

# there should probably a friend circle counter set to 0
# maybe a dictionary to keep track of.. each student's friends?

# it seems to have something to do with.. indexes and values
# if the [f1][f2] == 1 -> at least one friend circle
# if [f1][f2] == 0, no direct relationship.. check if indirect relationship?

# if there is NO relationship at all, increase the counter by 1
# hmm.. is it similar to overlapped meetings? looking for gaps in overlapped relationships.. then += circle
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        circles = 1
        direct_friends = {}
        not_friends = {}
        visited = set()
        
        for student_idx, student in enumerate(M):
            for relationship_idx, relationship in enumerate(student):
                if M[student_idx][relationship_idx] == 1:
                    if student_idx not in direct_friends:
                        direct_friends[student_idx] = [relationship_idx]
                    else:
                        direct_friends[student_idx].append(relationship_idx)
                if M[student_idx][relationship_idx] == 0:
                    if student_idx not in not_friends:
                        not_friends[student_idx] = [relationship_idx]
                    else:
                        not_friends[student_idx].append(relationship_idx)
                        
        print('direct_friends', direct_friends)
        print('not_friends', not_friends)
        for student in not_friends:
            if student in visited:
                break
                
            student_friends = direct_friends[student]
            strangers = not_friends[student]
            
            for friend in student_friends:
                visited.add(friend)
                
            print('student', student)
            print('visited', visited)
            print('student_friends', student_friends)
            print('strangers', strangers)
            
            for stranger in strangers:
                stranger_friends = direct_friends[stranger]
                visited.add(stranger)
                print('stranger', stranger)
                print('stranger_friends', stranger_friends)
                for idx, friend in enumerate(stranger_friends):
                    visited.add(friend)
                    print('idx', idx)
                    print('friend', friend)
                    if friend in student_friends:
                        print('MUTUAL FRIEND')
                        break
#                   if at end of list and no mutual friends, += circles
                    if idx == len(stranger_friends) - 1:
                        circles += 1
                        print(circles)
                        break
            print('\n')
        return circles


# failing
[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
# expect 1, getting 2
