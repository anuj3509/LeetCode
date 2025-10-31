class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        numSet = set()
        for num in nums:
            if num in numSet:
                res.append(num)
            else:
                numSet.add(num)
        return res