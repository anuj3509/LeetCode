class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        gaps.append(startTime[0] - 0)   # first gap = before the first meeting

        # intermediate gaps = between meetings
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])

        gaps.append(eventTime - endTime[-1])    # last gap = after the last meeting

        # merging max sum of any k+1 consecutive gaps - sliding window of k+1
        window_size = k + 1
        current_sum = sum(gaps[:window_size])
        max_gap = current_sum

        for i in range(window_size, len(gaps)):
            current_sum += gaps[i] - gaps[i - window_size]
            max_gap = max(max_gap, current_sum)

        return max_gap

    # TC: O(n)