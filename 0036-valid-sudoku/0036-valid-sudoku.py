class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)  # key = row[i]  ; value is a set containing the values
        col = collections.defaultdict(set)  # key = col[i]  ; value is a set containing the values
        box = collections.defaultdict(set)  # key = (row[i//3] , col[c//3]) ; value is a set containing the values

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r] or
                    board[r][c] in col[c] or
                    board[r][c] in box[r//3,c//3]):
                    return False
                else:
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    box[r//3,c//3].add(board[r][c])      
        return True