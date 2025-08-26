class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        max_diagonal, max_area = 0, 0
        for a, b in dimensions:
            cur = math.sqrt(a * a + b * b)
            if (cur > max_diagonal):
                max_diagonal = cur
                max_area = a * b
            elif cur == max_diagonal:
                max_area = max(max_area, a * b)
        return max_area