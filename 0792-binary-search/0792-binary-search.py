class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # m = (l + r) // 2    # Calculate the midway point inside the loop
            m = l + (r - l) // 2    # To prevent overflow in C++ and Java
            if target < nums[m]:
                r = m - 1   # Update the right pointer
            elif target > nums[m]:
                l = m + 1   # Update the left pointer
            else:
                return m    # return m if found targer
        return -1

