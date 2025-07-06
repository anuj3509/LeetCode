from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = -1
        # checking for each number if its frequency equals its value
        for num in count:
            if count[num] == num:
                res = max(res, num)
        return res
