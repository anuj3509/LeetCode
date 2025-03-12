class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = 0
        pos = 0

        # # TC: O(n)
        # for num in nums:
        #     if num < 0:
        #         neg += 1
        #     elif num > 0:
        #         pos += 1
        # return max(neg, pos)



        # Using Binary Search [TC: O(log n)]
        l = 0
        r = len(nums) - 1

        # Binary search to count negatives
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < 0:
                l = mid + 1  # Move RP to find first non-negative
            else:
                r = mid - 1  # Move LP to find first non-negative
        neg = l  

        l, r = 0, len(nums) - 1  # reset pointers

        # Binary search to count positives
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= 0:
                l = mid + 1  # Move RP to find first positive
            else:
                r = mid - 1  # Move LP if nums[mid] is positive
        pos = len(nums) - l  

        return max(neg, pos)