class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = 0
        res = []

        for bit in nums:
            curr = ((curr << 1) + bit) % 5
            res.append(curr == 0)
            
        return res