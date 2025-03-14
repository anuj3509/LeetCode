class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        total = sum(candies)
        if total < k:
            return 0

        # Search space for binary search: [1, sum/k]
        l = 1
        r = total // k
        res = 0

        while l <= r:
            m = (l + r) // 2
            count = 0       # count for each candidate
            for c in candies:
                if c >= m:
                    count += c // m
                if count >= k:
                    break
            if count >= k:
                res = m
                l = m + 1   # update the search space to look for larger values
            else:
                r = m - 1   # update the search space to look for larger values
        return res