class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # # Brute force approach double for loop, finding area using min of 
        # # both heights at lp and rp and [r-l] as the base
        
        # res = 0
        # for l in range(len(height)):
        #     for r in range(l+1, len(height)):
        #         area = (r-l) * min(height[l], height[r])
        #         res = max(res, area)
        # return res



        # Optimized approach: two pointers
        res = 0
        l = 0
        r = len(height)-1

        while l < r:
            area = (r-l)*min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

