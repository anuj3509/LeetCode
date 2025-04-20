from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        total = 0
        for x, v in cnt.items():
            group = x + 1
            # no. of full groups needed to cover v rabits
            num_groups = (v + group - 1) // group
            total += num_groups * group
        return total
