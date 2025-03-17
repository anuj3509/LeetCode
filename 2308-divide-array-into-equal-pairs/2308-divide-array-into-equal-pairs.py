class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        # # Using hashmap
        # count = {}  # hashmap
        # for num in nums:
        #     if num not in count:
        #         count[num] = 0
        #     count[num] += 1

        # for n,c in count.items():
        #     if c % 2:   # even count of each value
        #         return False
        # return True


        # Using hashset
        odd_set = set()

        for n in nums:
            if n not in odd_set:
                odd_set.add(n)
            else:
                odd_set.remove(n)
        return len(odd_set) == 0