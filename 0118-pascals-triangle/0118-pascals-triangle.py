class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]     # first row is just [1]
        
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0] # adding '0' at the beginning and the end of the prev row to compute next row
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1]) # computing the next row element by element
            res.append(row)
        return res

        # TC = O(n^2)