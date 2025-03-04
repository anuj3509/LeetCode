class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        # Math based greedy approach    ->     TC: O(log3(n))  ;   SC: O(n)
        # Find largest power of 3^i <= n
        i = 0
        while 3**(i+1) <= n:
            i += 1

        # greedy, remove largest powers
        while i >= 0:
            power = 3**i
            if power <= n:
                n -= power
            if power <= n:      # early stopping
                return False
            i -= 1
        return n == 0
        
        
        # # Backtracking approach
        # def backtrack(i, curr):
        #     if curr == n:
        #         return True
        #     if curr > n or 3**i > n:    # if current sum becomes large than the number or 3^i exceeds n
        #         return False

        #     # include case
        #     if backtrack(i + 1, curr + 3**i):
        #         return True
        #     # skip case
        #     return backtrack(i + 1, curr)
            
        # return backtrack(0, 0)