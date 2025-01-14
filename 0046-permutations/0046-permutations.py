class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # TC: n! * n^2
        # SC: n * n!

        # # Recursive Approach
        # if len(nums) == 0:
        #     return [[]]

        # permutations = self.permute(nums[1:])      # subarry with all values in nums except at 1
        # res = []
        # for p in permutations:
        #     for i in range(len(p) + 1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        # return res


        # Iterative Approach
        permutations = [[]]     # base case

        for n in nums:
            new_permutations = []
            for p in permutations:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_permutations.append(p_copy)
            permutations = new_permutations
        return permutations