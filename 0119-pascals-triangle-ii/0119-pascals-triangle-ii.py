class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = 0
        row = [1]
        while numRows != rowIndex:
            newRow = [1] * (len(row) + 1)
            for i in range(1, len(row)):
                newRow[i] = row[i] + row[i-1]
            row = newRow
            numRows += 1
        return row
