class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        n = right + 1
        primes = [True] * n
        primes[0] = primes[1] = False

        inf = 10 ** 5
        best = inf
        bestDelta = inf
        last = inf

        for k in range(2, n):
            current = k
            if primes[k]:
                if left <= k <= right:
                    if last != inf:
                        delta = k - last
                        if delta < bestDelta:
                            best = last
                            bestDelta = delta
                    last = k

                current = k * k
                while current < n:
                    primes[current] = False
                    current += k
        
        if best == inf:
            return [-1, -1]
        return [best, best + bestDelta]