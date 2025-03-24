class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        prev_end = 0
        for start, end in meetings:
            start = max(start, prev_end + 1)
            length = end - start + 1
            days -= max(length, 0)      # if the length is negative, we take 0 instead of negative days
            prev_end = max(prev_end, end)
        return days