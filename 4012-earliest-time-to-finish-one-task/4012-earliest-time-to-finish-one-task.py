class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        time = 0
        minTime = float("inf")

        for task in tasks:
            time = task[0] + task[1]
            minTime = min(minTime, time)
        return minTime