class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res  