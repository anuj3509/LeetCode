class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)  # Convert nums into a min-heap
        operations = 0
        
        while len(nums) > 1 and nums[0] < k:
            x = heappop(nums)  # Extract smallest
            y = heappop(nums)  # Extract second smallest
            new_val = min(x, y) * 2 + max(x, y)
            heappush(nums, new_val)  # Insert new value into heap
            operations += 1
        
        return operations if nums[0] >= k else -1  # If the last element is still < k, return -1
