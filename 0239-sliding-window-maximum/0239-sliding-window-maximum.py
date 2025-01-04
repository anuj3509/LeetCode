class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # # Brute Force solution where i find the max element in each window of length k
        # output = []
        # for i in range(len(nums) - k + 1):
        #     maxi = nums[i]
        #     for j in range(i, i+k):
        #         maxi = max(maxi, nums[j])
        #     output.append(maxi)

        # return output




        # Optimized solution using a deque
        output = []
        l = r = 0     #left and right pointers
        q = collections.deque()     #containing indices

        while r < len(nums):    # while the right pointer is still in bound
            while q and nums[q[-1]] < nums[r]:     # while the rightmost value is less than the value we are inserting
                q.pop()
            q.append(r)         # appending indices and will fetch the number later

            # remove left value from window if leftmost value is out of bounds of the window
            if l > q[0]:
                q.popleft()

            if (r+1) >= k:  #if our window is atleast size k
                output.append(nums[q[0]])
                l += 1  #left pointer will only increment once our window has reached size k
            r += 1      #right pointer will always increment

        return output


