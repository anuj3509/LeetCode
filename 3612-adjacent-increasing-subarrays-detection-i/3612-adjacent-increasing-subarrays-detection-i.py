class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True

        size = 1
        for i in range(1, len(nums) - k):
            j = i + k
            if nums[i] > nums[i-1] and nums[j] > nums[j-1]:
                size += 1
            else:
                size = 1
            j += 1

            if size == k:
                return True

        return False      