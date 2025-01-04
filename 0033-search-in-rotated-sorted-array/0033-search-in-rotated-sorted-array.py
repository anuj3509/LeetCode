class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:  # left sorted portion
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:   # nums[l] <= nums[m]    -->     right sorted portion
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            


            # if target > nums[m] and target >= nums[r]:
            #     l = m + 1
            # elif target > nums[m] and target < nums[r]:
            #     r = m - 1
            # elif target < nums[m] and target >= nums[l]:
            #     r = m - 1
            # elif target < nums[m] and target < nums[l]:
            #     l = m + 1
            # else:
            #     return m



        return -1
            