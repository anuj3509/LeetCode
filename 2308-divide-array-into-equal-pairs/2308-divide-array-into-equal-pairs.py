class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}  # hashmap
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for n,c in count.items():
            if c % 2:   # even count of each value
                return False
        return True