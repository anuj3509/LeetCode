class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        n2 = (n + 1) // 2
        res = 0
        seen = set()
        for v in range(10 ** (n2 - 1), 10 ** n2):
            vv = str(v) + str(v)[::-1][n % 2:]
            key = ''.join(sorted(vv))
            if int(vv) % k == 0 and key not in seen:
                seen.add(key)
                count = Counter(vv)
                x = (n - count['0']) * factorial(n - 1)
                for i,c in count.items():
                    x //= factorial(c)
                res += x
        return res