class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:   # for large n, the prob approaches 1
            return 1.0

        # scaling by modeling servings in 25ml unit
        m = math.ceil(n / 25)
        dp = {}

        def solve(a, b):
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1.0
            if b <= 0: return 0.0
            if (a, b) in dp: return dp[(a, b)]

            # calc prob from the 4 serving options
            dp[(a, b)] = 0.25 * (
                solve(a - 4, b) +
                solve(a - 3, b - 1) +
                solve(a - 2, b - 2) +
                solve(a - 1, b - 3)
            )
            return dp[(a, b)]

        return solve(m, m)
