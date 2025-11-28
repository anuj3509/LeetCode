class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        for i in range(1, n+1):
            print(i)
            if (i*(i+1)) / 2 == ((n*(n+1)) / 2) - (((i-1)*i) / 2):  # i-1 because the pivot is inclusive in sum for both sides
                return i
        return -1