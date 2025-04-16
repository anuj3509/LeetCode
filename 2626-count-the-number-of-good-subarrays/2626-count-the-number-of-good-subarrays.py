class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)  # frequency dict for window elements
        res = 0
        left = 0
        curr_pairs = 0

        # expand the window with the right pointer
        for right in range(n):
            x = nums[right]
            # when adding element x, every occurrence already in the window
            # forms a new pair with the new x
            curr_pairs += freq[x]
            freq[x] += 1

            # once the condition is satisfied, contract from the left
            while curr_pairs >= k and left <= right:
                # all subarrays starting at left with an end index >= right are good
                res += (n - right)
                
                # remove the element at left from the window and update pair count
                x_left = nums[left]
                freq[x_left] -= 1
                # removing one instance of x_left removes (freq[x_left]) pairs
                curr_pairs -= freq[x_left]
                left += 1
        return res