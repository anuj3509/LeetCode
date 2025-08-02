class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26  # storing frequency of 'a' to 'z'

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        max_odd = float('-inf')
        min_even = float('inf')

        for f in freq:
            if f > 0:
                if f % 2 == 1:
                    max_odd = max(max_odd, f)
                else:
                    min_even = min(min_even, f)

        #  no odd or even frequencies are found -> return 0
        if max_odd == float('-inf') or min_even == float('inf'):
            return 0

        return max_odd - min_even