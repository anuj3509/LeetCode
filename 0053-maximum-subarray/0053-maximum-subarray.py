class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]   # default value for the max sum
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0     # if current sum goes negative, reset it
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
        return max_sub