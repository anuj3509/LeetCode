class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = bank[0].count("1")   # count no of lasers in the first row

        for i in range(1, len(bank)):
            curr = bank[i].count("1")
            if curr > 0:
                res += (prev * curr)    # no of laser beams between two layers
                prev = curr
        return res