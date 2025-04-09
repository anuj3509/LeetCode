class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Check if there is any number less than k. If so, return -1 because we cannot increase numbers.
        if min(nums) < k:
            return -1
        
        # Count the distinct numbers in nums that are strictly greater than k.
        distinct_above_k = {x for x in nums if x > k}
        
        # The number of operations needed is exactly the number of distinct values above k.
        return len(distinct_above_k)
