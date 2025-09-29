class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # maxPerimeter = perimeter = 0

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] > nums[k] and nums[k] + nums[j] > nums[i] and nums[i] + nums[k] > nums[j]:
        #                 perimeter = nums[i] + nums[j] + nums[k]
        #                 maxPerimeter = max(perimeter, maxPerimeter)
        # return maxPerimeter


        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0