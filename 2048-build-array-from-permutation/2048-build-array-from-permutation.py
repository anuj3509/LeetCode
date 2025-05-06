class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # encode: new_val = nums[nums[i]] % n,
        # then store combined = old + n*new_val
        for i in range(n):
            nums[i] += n * (nums[nums[i]] % n)
        
        # extract the new values
        for i in range(n):
            nums[i] //= n
        return nums
