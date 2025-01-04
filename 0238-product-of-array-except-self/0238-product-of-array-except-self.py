class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # #------------ Brute Force Approach ----------
        # n = len(nums)
        # res = [0] * n   #the result array of size n corresponding to input size n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]

        #     res[i] = prod

        # return res


        #------------ Optimal Approach using prefix and postfix----------
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        post = [0] * n

        pref[0] = post[n-1] = 1

        for i in range(1,n):                #loop to calculate prefix product
            pref[i] += nums[i-1]*pref[i-1]
        for i in range(n-2, -1, -1):        #loop to calculate postfix product
            post[i] += nums[i+1]*post[i+1]
        
        for i in range(n):
            res[i] = pref[i]*post[i]

        return res