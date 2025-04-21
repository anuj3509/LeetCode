class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mn = mx = cur = 0
        for d in differences:
            cur += d
            mn = min(mn, cur)
            mx = max(mx, cur)
        low = lower - mn
        high = upper - mx
        return max(0, high - low + 1)