class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if remain == 0:     # remainder is already 0, we return 0
            return 0

        res = len(nums)
        curr_sum = 0

        # map remain of prefix sums to last idx
        remain_to_idx = {
            0 : -1
        }

        for i, n in enumerate(nums):
            # remain + x = curr_sum     ::      x = curr_sum - remain
            curr_sum = (curr_sum + n) % p
            prefix = (curr_sum - remain + p) % p
            if prefix in remain_to_idx:
                length = i - remain_to_idx[prefix]
                res = min(res, length)
            remain_to_idx[curr_sum] = i


        return -1 if res == len(nums) else res