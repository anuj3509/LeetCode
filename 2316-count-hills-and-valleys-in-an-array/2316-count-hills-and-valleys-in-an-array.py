class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0

        # removing adjacent duplicates
        filtered = [nums[0]]
        for num in nums[1:]:
            if num != filtered[-1]:
                filtered.append(num)

        for i in range(1, len(filtered) - 1):
            # hill
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1  

            # valley
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1

        return count