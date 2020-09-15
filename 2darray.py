"""
Hackerrank Interview Prep - Arrays

Given a 6 x 6 array, there are 16 hour glasses

Calculate sum of every hour glass and return max sum. 
"""

# thoughts
# create empty max_sum

# establish the configuration of the hour glass -> helper function
# traverse through the 2d array 
# have an empty sum variable
# get the configuration and add each element to the sum
# if the sum is > max_sum or max_sum is none, set max_sum to sum

# return the max_sum 



def max_sum(grid):
    maximum_sum = None 
    
    for value in hourglass_sums(grid):
        if maximum_sum == None or value > maximum_sum:
            maximum_sum = value
        
    return maximum_sum

# thoughts on configuration
# grid -> [row][col]
# grid[0][0], grid[0][1], grid[0][2]
# grid[1][1]
# grid[2][0], grid[2][1], grid[2][2]
def hourglass_sums(grid):
    # configuration of hourglass isss
    values = []
    row = 0
    while row < len(grid) -  2:

        col = 0
        while col < len(grid[row]) - 2:
            hourglass_sum = 0

            hourglass_sum += grid[row][col]
            hourglass_sum += grid[row][col + 1]
            hourglass_sum += grid[row][col + 2]
            hourglass_sum += grid[row + 1][col + 1]
            hourglass_sum += grid[row + 2][col]
            hourglass_sum += grid[row + 2][col + 1]
            hourglass_sum += grid[row + 2][col + 2]
            
            values.append(hourglass_sum)
            col += 1
        
        row += 1

    return values

# Test Cases

grid1 = [
[-9, -9, -9, 1, 1, 1],
[0, -9, 0, 4, 3, 2],
[-9, -9, -9, 1, 2, 3],
[0, 0, 8, 6, 6, 0],
[0, 0, 0, -2, 0, 0],
[0, 0, 1, 2, 4, 0]
]
"""
Expected output:
-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18

result = 28
"""
grid2 = [
[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]
]
print(max_sum(grid2))