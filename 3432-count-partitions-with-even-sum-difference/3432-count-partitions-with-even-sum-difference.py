class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        count = 0
        
        for i in range(1, len(nums)):
            sum_left = 0
            sum_left += nums[i]
            if abs(sum_left - (total - sum_left)) % 2 == 0:
                print(sum_left, total)
                count += 1
        return count