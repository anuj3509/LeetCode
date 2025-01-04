class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping character count of each string with list of anagrams

        for s in strs:
            count = [0]*26  #a, b, c, ... z

            for c in s:
                count[ord(c)-ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())