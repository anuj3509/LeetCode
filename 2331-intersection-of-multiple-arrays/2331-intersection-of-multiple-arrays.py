class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = []
        numOfArrays = len(nums)   # number of arrays in nums
        digit_map = {}
        
        for subarr in nums:
            for digit in subarr:
                digit_map[digit] = 1 + digit_map.get(digit,0)
        
        for digit in digit_map:
            if digit_map.get(digit,0) == numOfArrays:
                res.append(digit)
                
        return sorted(res)