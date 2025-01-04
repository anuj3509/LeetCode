class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # Binary search to find which row could have the element
        top, bot = 0, rows - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:    # check the rightmost value in the row
                top = row + 1
            elif target < matrix[row][0]:    # check the leftmost value in the row
                bot = row - 1
            else:
                break

        # First condition is when we crossed out every row in the matrix and no raw had the target
        if not (top <= bot):
            return False
        # Running binary search on the row which we found
        desired_row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
