class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        visited = set()
        for i in range(len(nums) - 1,  -1, -1):
            if nums[i] in visited:
                return i // 3 + 1
            visited.add(nums[i])
        return 0




        # # TC = SC = O(n)

        # n = len(nums)
        # d = {}

        # # Build frequency dictionary
        # for x in nums:
        #     d[x] = d.get(x, 0) + 1
        # dup = 0

        # # Count numbers that appear more than once
        # for v in d.values():
        #     if v > 1:
        #         dup += 1
        
        # if dup == 0:
        #     res = 0
        # else:
        #     op = 0
        #     i = 0
        #     # Remove elements in blocks of 3 until all remaining are distinct
        #     while i < n:
        #         for _ in range(3):
        #             if i >= n:
        #                 break
        #             x = nums[i]
        #             d[x] -= 1
        #             if d[x] == 1:
        #                 dup -= 1
        #             i += 1
        #         op += 1
        #         if dup == 0:
        #             break
        #     res = op
        # return res