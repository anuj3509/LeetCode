class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        # maximum possible number of distinct values in a divisibility chain
        maxK = int(math.log2(maxValue)) + 1

        # precompute divisors < v for every v
        divs = [[] for _ in range(maxValue+1)]
        for d in range(1, maxValue+1):
            for m in range(2*d, maxValue+1, d):
                divs[m].append(d)

        # dp[v] = number of distinct-length-k chains ending at v (start with k=1)
        dp = [1] * (maxValue+1)

        # precompute factorials & inverses up to n for binomial coeffs
        fact = [1] * (n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i % MOD
        inv = [1] * (n+1)
        inv[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            inv[i-1] = inv[i] * i % MOD
        def C(a: int, b: int) -> int:
            if b < 0 or b > a: 
                return 0
            return fact[a] * inv[b] % MOD * inv[a-b] % MOD

        res = 0
        # for each possible number k of distinct values in the array
        for k in range(1, maxK+1):
            # sum of all chains of length k
            total_chains = sum(dp[1:]) % MOD
            # choose positions for the k distinct values in an array of length n
            res = (res + total_chains * C(n-1, k-1)) % MOD

            # build dp for chains of length k+1
            ndp = [0] * (maxValue+1)
            for v in range(1, maxValue+1):
                for d in divs[v]:
                    ndp[v] = (ndp[v] + dp[d]) % MOD
            dp = ndp

        return res
