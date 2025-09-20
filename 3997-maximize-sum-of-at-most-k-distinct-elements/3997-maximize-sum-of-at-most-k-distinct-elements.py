class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # numSet = set(nums)
        # while len(numSet) > k:
        #     numSet.remove(min(numSet))
        # return sorted((list(numSet)), reverse = True)


        # ----------- Single line approach -----------
        return sorted((list(set(nums))), reverse = True)[:k]