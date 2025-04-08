class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
        dup = 0
        for v in d.values():
            if v > 1:
                dup += 1
        if dup == 0:
            res = 0
        else:
            op = 0
            i = 0
            while i < n:
                for _ in range(3):
                    if i >= n:
                        break
                    x = nums[i]
                    d[x] -= 1
                    if d[x] == 1:
                        dup -= 1
                    i += 1
                op += 1
                if dup == 0:
                    break
            res = op
        return res
