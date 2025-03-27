class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        # Boyer - Moore Voting Algorithm [TC: O(n) ; SC: O(1)]
        majority = 0
        count = 0

        for n in nums:
            if count == 0:
                majority = n
            if n == majority:
                count += 1
            else:
                count -= 1

        leftcount = 0
        rightcount = nums.count(majority)

        for i in range(len(nums)):
            if nums[i] == majority:
                leftcount += 1
                rightcount -= 1
            left_len = i + 1
            right_len = len(nums) - 1 - i

            # Check for presence of majority element
            if 2 * leftcount > left_len and 2 * rightcount > right_len:
                return i
        return -1
        
        
        
        # # Using Hashmap     [TC: O(n) ; SC: O(n)]
        # left = defaultdict(int)     # hashmap
        # right = Counter(nums)

        # for i in range(len(nums)):
        #     left[nums[i]] += 1
        #     right[nums[i]] -= 1
        #     left_len = i + 1
        #     right_len = len(nums) - 1 - i

        #     # Check for presence of majority element
        #     if 2 * left[nums[i]] > left_len and 2 * right[nums[i]] > right_len:
        #         return i
        # return -1