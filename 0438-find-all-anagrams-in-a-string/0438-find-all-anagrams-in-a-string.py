class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        char_map = {}
        
        # build freq map for string p
        for char in p:
            char_map[char] = char_map.get(char, 0) + 1
        
        i, j = 0, 0
        n = len(s)
        count = len(char_map)
        
        while j < n:
            char = s[j]
            
            # increase window
            if char in char_map:
                char_map[char] -= 1
                if char_map[char] == 0:
                    count -= 1
            
            # decrease window if size > len(p)
            if j - i + 1 > len(p):
                left = s[i]
                if left in char_map:
                    if char_map[left] == 0:
                        count += 1
                    char_map[left] += 1
                i += 1
            
            # chekc if current window is anagram
            if count == 0 and j - i + 1 == len(p):
                result.append(i)
            
            j += 1
        
        return result