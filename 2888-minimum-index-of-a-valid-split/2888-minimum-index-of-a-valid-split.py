class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        # TC: O(n) ; SC: O(n)
        left = defaultdict(int)     # hashmap
        right = Counter(nums)

        for i in range(len(nums)):
            left[nums[i]] += 1
            right[nums[i]] -= 1
            left_len = i + 1
            right_len = len(nums) - 1 - i

            # Check for presence of majority element
            if 2 * left[nums[i]] > left_len and 2 * right[nums[i]] > right_len:
                return i
        return -1


        # Boyer - Moore Voting Algorithm [TC: O(n) ; SC: O(1)]