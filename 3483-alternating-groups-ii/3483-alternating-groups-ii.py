class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        # Sliding window approach
        n = len(colors)
        l = 0
        res = 0

        for r in range(1, n + k - 1):
            if colors[r % n] == colors[(r-1) % n]:      # not alternating
                l = r                                   # we expand our window
            if r - l + 1 > k:       # this ensures that the window is newer greater than k by 1
                l += 1
            if r - l + 1 == k:
                res += 1
        return res