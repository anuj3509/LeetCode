class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0

        # # Brute force approach: TC = O(n^3)

        # if len(nums) < 3: return 0
        # for j in range(i+1, len(nums)):
        #     for k in range(j+1, len(nums)):
        #         if nums[j] + nums[k] > nums[i] and nums[i] + nums[k] > nums[j] and nums[j] + nums[i] > nums[k]:
        #             res += 1
        # return res



        # Optimized approach using sorting and Binary Search: TC = O(n^2)
        
        # c < a + b : triangle condition

        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            start, end = 0, i-1

            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    res += end - start
                    end -= 1
                elif nums[start] + nums[end] <= nums[i]:
                    start += 1
        return res