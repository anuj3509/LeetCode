class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4500:   # for large n, the prob approaches 1 (hardcoded this 'n' value after many failed testcases)
            return 1

        # scaling by modeling servings in 25ml unit
        # m = math.ceil(n / 25)
        dp = {}

        def solve(a, b):
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1
            if b <= 0: return 0
            if (a, b) in dp: return dp[(a, b)]

            # calc prob from the 4 serving options
            dp[(a, b)] = 0.25 * (
                solve(a - 100, b) +
                solve(a - 75, b - 25) +
                solve(a - 50, b - 50) +
                solve(a - 25, b - 75)
            )
            return dp[(a, b)]

        return solve(n, n)
