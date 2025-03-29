class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        MOD = 10**9 + 7
        res = 1

        prime_scores = []
        for n in nums:
            score = 0
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    score += 1
                    while n % f == 0:
                        n = n // f
            if n >= 2:
                score += 1
            prime_scores.append(score)

        leftbound = [-1] * N
        rightbound = [N] * N

        stack = []  # indixes of decreasing or equal order scores
        for i, s in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < s:
                index = stack.pop()
                rightbound[index] = i
            if stack:
                leftbound[i] = stack[-1]
            stack.append(i)

        minheap = [(-n, i) for i, n in enumerate(nums)]     # num, index to heap
        heapify(minheap)

        while k > 0:
            n, index = heappop(minheap)
            n = -n
            score = prime_scores[index]

            left_cnt = index - leftbound[index]
            right_cnt = rightbound[index] - index

            count = left_cnt * right_cnt
            operations = min(count, k)
            res = (res * pow(n, operations, MOD)) % MOD
            k -= operations
        
        return res