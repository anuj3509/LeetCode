class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # TC: O(n)    ;   SC: O(1)
        lastindex = {}      # char : last index in s

        # building our hashmap to map each character to its last index in the string
        for i, c in enumerate(s):
            lastindex[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastindex[c])
            if i == end:
                res.append(size)
                size = 0
        return res