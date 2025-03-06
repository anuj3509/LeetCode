class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dim = len(grid)
        count = defaultdict(int)

        for i in range(dim):
            for j in range(dim):
                count[grid[i][j]] += 1
        
        double, missing = 0, 0

        for num in range(1, dim*dim + 1):
            if count[num] == 0:
                missing = num
            if count[num] == 2:
                double = num
        return [double, missing]