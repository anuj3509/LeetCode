class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        def backtrack(i, curr):
            if curr == n:
                return True
            if curr > n or 3**i > n:    # if current sum becomes large than the number or 3^i exceeds n
                return False

            # include case
            if backtrack(i + 1, curr + 3**i):
                return True
            # skip case
            return backtrack(i + 1, curr)

        return backtrack(0, 0)