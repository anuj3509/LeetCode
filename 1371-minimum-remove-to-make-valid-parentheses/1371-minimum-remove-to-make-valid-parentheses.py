class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0   # extra open parenthesis
        for c in s:
            if c =="(":
                res.append(c)
                count += 1
            elif c == ")" and count > 0:
                res.append(c)
                count -= 1
            elif c != ")":
                res.append(c)
        
        filtered = []
        # go through all the characters in res in reverse order to 
        # remove extra open parenthesis starting from the end
        for c in res[::-1]:
            if c == "(" and count > 0:
                count -= 1
            else:
                filtered.append(c)
        return "".join(filtered[::-1])