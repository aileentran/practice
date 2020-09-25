"""
Leetcode: 79. Word Search
"""
# Notes
# input: 2d array of letters, word string
# output: boolean - true if can find the word, false otherwise

# current = board[row][col]
# up = board[row + 1][col]
# down = board[row - 1][col]
# left = [row][col - 1]
# right = [row][col + 1]

# loop through rows to find first letter
# after find first letter, look around (up, down, left, right); NO diagonals(?)
# if find it, move into the it and repeat


# might want to fail early? if it fails at any step, return false
# if can go through the whole thing and find the word, return true

# CURR STATUS
# can find match but dictionary of directions stays static 

def exist(self, board: List[List[str]], word: str) -> bool:
    given = ""
    start = [0, 0] #[row, col]
    
#       finding the starting idxs
    for row_idx, row in enumerate(board):
        if word[0] in row:
            col_idx = row.index(word[0])
            curr = [row_idx, col_idx]
            given += board[row_idx][col_idx]
            break
            
    if len(given) == 0:
        return False
    
    while True:
        if given == word:
            return True
        
        curr_row, curr_col = start
        directions = {
            'up': [curr_row - 1, curr_col],
            'down': [curr_row + 1, curr_col],
            'left':[curr_row, curr_col - 1],
            'right':[curr_row, curr_col + 1]
        }
        
        for char in word[1:]:
            print('char', char)
            for direction in directions:
                row, col = directions[direction]
                if row < 0 or col < 0:
                    continue
                if char == board[row][col]:
                    given += board[row][col]
                    curr_row, curr_col = row, col
                    print('MATCH!')
                    print(given)
                    # print(curr)
                    break
            print(directions)
        return 