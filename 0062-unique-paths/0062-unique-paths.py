class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n   # last row
        
        for i in range(m-1):    # iterate through all wows except last row
            newRow = [1] * n
            for j in range(n-2, -1, -1):    # go through every col except rightmost column [because it is always going to be 1]
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

        # TC: O(n * m)
        # SC: O(n)