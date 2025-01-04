class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s =set(nums)
        longest = 0
        for num in s:
            if num -1 not in s:
                length=0
                while num+length in s:
                    length += 1
                longest = max(longest,length)
        return longest


# Some cases are failing in this

        # s =set(nums)
        # longest = 1
        # if s == []:
        #     return 0
        # for num in s:
        #     if num -1 not in s:
        #         curr = 1
        #         while num + 1 in s:
        #             curr += 1
        #             num += 1
        #             longest = max(longest, curr)
        # return longest