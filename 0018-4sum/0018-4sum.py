class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # val1 = nums[i]
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                # val2 = nums[j]
                # diff = target - nums[i] - nums[j]

                l, r = j+1, n-1
                while l < r:
                    fsum = nums[i] + nums[j] + nums[l] + nums[r]

                    if fsum > target:
                        r -= 1
                    elif fsum < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l-1] and l<r:
                            l += 1
                        while nums[r] == nums[r+1] and l<r:
                            r -= 1
        return res
