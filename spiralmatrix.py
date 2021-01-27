"""
Leetcode - spiral matrix

input: 2d array of nums
output: list of nums in spiral order; 1st is [0][0] last is the center

Notes:
frame things with row beginning/row end and col beginning/col end
beginnings we move +1 and ends -1 as we go clockwise
"""
def spiralOrder(matrix):
    order = []
    row_begin = 0
    row_end = len(matrix)
    col_begin = 0
    col_end = len(matrix[0])

    while row_end > row_begin and col_end > col_begin:
        # going to the right!
        # print('right')
        for col in range(col_begin, col_end):
            # print(matrix[row_begin][col])
            order.append(matrix[row_begin][col])

        # going down
        # print('down')
        for row in range(row_begin + 1, row_end):
            # print(matrix[row][col_end - 1])
            order.append(matrix[row][col_end - 1])

        #going left
        if row_end - 1 != row_begin:
            # print('left')
            for col in range(col_end - 2, col_begin - 1, -1):
                print(matrix[row_end - 1][col])
                order.append(matrix[row_end - 1][col])

        # going up
        if col_end - 1 != col_begin:
            # print('up')
            for row in range(row_end - 2, row_begin, -1):
                # print(matrix[row][col_begin])
                order.append(matrix[row][col_begin])

        row_begin += 1
        row_end -= 1
        col_begin += 1
        col_end -= 1

    return order
matrix = [[1,2,3],[4,5,6]] #[1, 2, 3, 6, 5, 4]
matrix1 = [[1,2,3],[4,5,6],[7,8,9]] #[1,2,3,6,9,8,7,4,5]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] #[1,2,3,4,8,12,11,10,9,5,6,7]

print(spiralOrder(matrix))
print(spiralOrder(matrix1))
print(spiralOrder(matrix2))
