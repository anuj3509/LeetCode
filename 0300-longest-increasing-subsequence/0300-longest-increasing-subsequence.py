class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)    # longest increasing subsequence

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:       # this condition has to be true if you want it to be LIS
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

        # TC: O(n^2)
        # Better solution possible: O(n*logn)   ->  Binary Search