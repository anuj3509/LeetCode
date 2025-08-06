class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxNum = 0
        minNum = float("inf")

        strNum = str(num)

        for start in range(0, 10):
            for end in range(0, 10):
                if start != end:
                    x = int(strNum.replace(str(start), str(end)))

                    maxNum = max(x, maxNum)
                    minNum = min(x, minNum)

        return maxNum - minNum