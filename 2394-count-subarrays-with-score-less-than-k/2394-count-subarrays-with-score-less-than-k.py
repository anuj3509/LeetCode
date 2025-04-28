class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0
        l = 0
        for r, v in enumerate(nums):
            s += v
            # shrink until window score < k
            while l <= r and s * (r - l + 1) >= k:
                s -= nums[l]
                l += 1
            # all subarrays ending at r starting from l…r are valid
            ans += r - l + 1
        return ans
