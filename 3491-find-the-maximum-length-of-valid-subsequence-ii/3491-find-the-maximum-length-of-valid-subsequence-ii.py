class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        best = 1                              # a single element subseq

        for i in range(n):
            for j in range(i):
                m = (nums[j] + nums[i]) % k   # residue fixed by (j, i)
                prev = dp[j].get(m, 1)        # 1 => start a fresh pair
                cand = prev + 1               # extend by nums[i]

                if cand > dp[i][m]:
                    dp[i][m] = cand
                    best = max(best, cand)

        return best
