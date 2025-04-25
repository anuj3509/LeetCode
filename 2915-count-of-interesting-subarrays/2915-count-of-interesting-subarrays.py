class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1     # one way to have zero matches before we start
        res = 0
        cnt = 0     # running count of nums[i] % modulo == k
        
        for x in nums:
            if x % modulo == k:
                cnt += 1    # increment when this element “matches”
            r = cnt % modulo
            
            # we want previous prefix r_pre such that (r - r_pre) % modulo == k
            # i.e. r_pre == (r - k) % modulo
            want = (r - k) % modulo
            res += freq[want]
            freq[r] += 1
        return res