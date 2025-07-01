class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        i = 0
        result = 1
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            group_len = j - i
            if group_len >= 2:
                result += (group_len - 1)  # removing one of the duplicates, one at a time
            i = j

        return result
