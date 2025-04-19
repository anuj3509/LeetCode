class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        
        def countLeq(target: int) -> int:
            cnt = 0
            l, r = 0, n-1
            while l < r:
                if nums[l] + nums[r] <= target:
                    cnt += r - l
                    l += 1
                else:
                    r -= 1
            return cnt
        
        return countLeq(upper) - countLeq(lower - 1)
