class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t) #this will sort the arrays and return true if both the
        # arrays are exactly same

        # return Counter(s) == Counter(t) #this is an inbuilt data structure in python which 
        # creates a hashmap and compares the key, value pair internally and returns true if 
        # both the counters are exactly same

# the below solution creates two hashmaps and compares them. it returns true if they are same
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True