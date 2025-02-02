class Solution:
    def fib(self, n: int) -> int:

        # # Recursive backtracking
        # if n == 0: return 0
        # if n == 1: return 1
        # return self.fib(n-1) + self.fib(n-2)


        # Dynamic Programming approach
        if n < 2: return n
        prev, curr = 0, 1
        for i in range(2, n + 1):
            prev, curr = curr, curr + prev
        return curr