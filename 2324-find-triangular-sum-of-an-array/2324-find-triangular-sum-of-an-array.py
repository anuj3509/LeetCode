class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        while len(nums) != 1:
            newNums = []
            for i in range(1, len(nums)):
                newNums.append((nums[i] + nums[i-1]) % 10)
            nums = newNums
        return nums[0]