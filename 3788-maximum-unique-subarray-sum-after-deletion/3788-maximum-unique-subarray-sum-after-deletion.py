class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positiveNumbers = set()
        for num in nums:
            if num > 0:
                positiveNumbers.add(num)
        
        if len(positiveNumbers) == 0:
            return max(nums)
        else:
            return sum(positiveNumbers)