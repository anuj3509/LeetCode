class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = 0
        pos = 0

        for num in nums:
            if num < 0:
                neg += 1
            elif num > 0:
                pos += 1

        return max(neg, pos)


        # l = 0
        # r = len(nums) - 1

        # if nums[l] == 0 or nums[r] == 0:
        #     return len(nums) - 1
        # if nums[l] > 0 or nums[r] < 0:
        #     return len(nums)

        # while l < r:
        #     # if nums[l] == 0 or nums[r] == 0:
        #     #     continue
        #     if nums[l] < 0:
        #         neg += 1
        #         l += 1
        #     if nums[r] > 0:
        #         pos += 1
        #         r -= 1
        #     if nums[l] == 0:
        #         r -= 1
        #     if nums[r] == 0:
        #         l += 1
        # return max(neg, pos)
