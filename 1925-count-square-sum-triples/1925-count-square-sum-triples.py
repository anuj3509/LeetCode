class Solution:
    def countTriples(self, n: int) -> int:
        res = 0

        for a in range(1, n):
            for b in range(1, n):
                square = int(a**2 + b**2)
                c = int(sqrt(square))
                if c**2 == square and c <= n:
                    res += 1
                    print(a, b, c)
        return res