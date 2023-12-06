from typing import List
class Solution:
    def __init__(self):
        pass
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def p_rint():
            for i in board:
                print(i)


        row_map =  {i: set() for i in range(9)}
        col_map =  {i: set() for i in range(9)}
        grid_map = {i: set() for i in range(9)}

        for i in range(9):
            print(f'{col_map=}')
            for j in range(9): 
                grid_pos = (i // 3) * 3 + (j // 3)
                val = board[i][j]
                if val != '.':
                    # handle unique row
                    if val in row_map[i]:
                        return False
                    else:
                        row_map[i].add(val)

                    # handle unique col
                    if val in col_map[j]:
                        return False
                    else:
                        col_map[j].add(val)

                    # handle unique subgrid
                    if val in grid_map[grid_pos]:
                        return False
                    else:
                        grid_map[grid_pos].add(val)
        return True

'''
0 - 2     3 - 6      7 - 9 (* 3)
 0 - 2     0 - 2      0 - 2
 3 - 6     3 - 6      3 - 6
 7 - 9     7 - 9      7 - 9

'''

board  = [["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          [".",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          ["8","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]

sol = Solution()
print(sol.isValidSudoku(board))
