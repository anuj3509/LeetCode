class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        # Sieve of Eratosthenes algorithm to find prime numbers { TC: O(log(log(n))) }
        def getPrimes():
            isPrime = [True] * (right + 1)
            isPrime[0] = isPrime[1] = False
            
            for n in range(2, int(sqrt(right)) + 1):
                if not isPrime[n]:
                    continue
                for m in range(n + n, right + 1, n):
                    isPrime[m] = False
            primes = []
            for i in range(len(isPrime)):
                if isPrime[i] and i >= left:
                    primes.append(i)
            return primes
        


        primes = getPrimes()    # gets all primes from [left, right]
        res = [-1, -1]
        diff = right - left + 1

        for i in range(1, len(primes)):
            if primes[i] - primes[i-1] < diff:
                diff = primes[i] - primes[i-1]
                res = [primes[i-1], primes[i]]
        return res 
        
        
        
        
        
        
        
        
        
        # n = right + 1
        # primes = [True] * n
        # primes[0] = primes[1] = False

        # inf = 10 ** 4
        # best = inf
        # bestDelta = inf
        # last = inf

        # for k in range(2, n):
        #     current = k
        #     if primes[k]:
        #         if left <= k <= right:
        #             if last != inf:
        #                 delta = k - last
        #                 if delta < bestDelta:
        #                     best = last
        #                     bestDelta = delta
        #             last = k

        #         current = k * k
        #         while current < n:
        #             primes[current] = False
        #             current += k
        
        # if best == inf:
        #     return [-1, -1]
        # return [best, best + bestDelta]