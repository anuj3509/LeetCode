import collections
import bisect
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        if n < 3:
            return 0

        value_to_indices = collections.defaultdict(list)
        for index, value in enumerate(nums):
            value_to_indices[value].append(index)
        count = 0

        # iterate through middle value index j
        for j in range(n):
            val_j = nums[j]
            target_val = val_j * 2

            if target_val in value_to_indices:
                target_indices = value_to_indices[target_val]
                left_count = bisect.bisect_left(target_indices, j)
                right_count = len(target_indices) - bisect.bisect_right(target_indices, j)
            
                # total triplets are product of found values on left and right which will generate all permutations
                count = (count + left_count * right_count) % MOD
            
        return count