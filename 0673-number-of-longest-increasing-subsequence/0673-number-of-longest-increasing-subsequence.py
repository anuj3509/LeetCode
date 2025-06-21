class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        dp = {}     # key, index, value = [lenght of LIS value]
        lenLIS, res = 0, 0      # lenght of LIS, count of LIS

        for i in range(len(nums) - 1, -1, -1):
            maxLength, maxCount = 1, 1     # length and count of LIS start from i

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:   # make sure increasing order
                    length, count = dp[j]       # length, count of LIS start from j
                    if length + 1 > maxLength:
                        maxLength, maxCount = length + 1, count
                    elif length + 1 == maxLength:
                        maxCount += count
            
            if maxLength > lenLIS:
                lenLIS, res = maxLength, maxCount
            elif maxLength == lenLIS:
                res += maxCount

            dp[i] = [maxLength, maxCount]

        return res