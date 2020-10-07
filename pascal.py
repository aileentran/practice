"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

def generate(numRows):
#       fail if numRows == 0 or -1
#       maybe return triangle for numRows of 1 or 2

    if numRows == 0:
        return None
    
    if numRows == 1:
        return [[1]]
    
    if numRows == 2:
        return [[1], [1, 1]]
    
    triangle = [[1], [1, 1]]
    
    i = 1
    
    while i < numRows - 1:
        row = triangle[i]
        next_row = [1]
        k = 0
        while k < len(row) - 1:
            num1 = row[k]
            num2 = row[k + 1]
            next_row.append(num1 + num2)
            
            # print(num1)
            # print(num2)
            # print(next_row)
            k += 1
        next_row.append(1)
        triangle.append(next_row)
        # print(triangle)
        i += 1
    return triangle


#Test
rows = 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
print(generate(rows))