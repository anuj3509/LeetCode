class Solution:
    def triangleType(self, nums: List[int]) -> str:
        triangle_set = set(nums)
        # checking if its possible to make trianle
        if (nums[0] + nums[1] <= nums[2]) or (nums[1] + nums[2] <= nums[0]) or (nums[0] + nums[2] <= nums[1]):
            return "none"

        if len(triangle_set) == 1:
            return "equilateral"
        elif len(triangle_set) == 2:
            return "isosceles"
        elif len(triangle_set) == 3:
            return "scalene"