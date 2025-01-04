class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # # Normal approach -- reversing string and comparing
        # str1 =''
        
        # for char in s:
        #     if char.isalnum():
        #         str1 += char.lower()
        # return str1 == str1[::-1]



        # ## two pointer approach
        # str1 =''

        # for char in s:
        #     if char.isalnum():
        #         str1 += char.lower()

        # lp,rp = 0 , len(str1)-1

        # while lp < rp:

        #     if str1[lp] != str1[rp]:
        #         return False
        #     else:
        #         lp += 1
        #         rp -= 1
        # return True





        # two pointer approach without using extra memory
        ## two pointer approach
        lp,rp = 0 , len(s)-1

        while lp < rp:

            while lp<rp and not s[lp].isalnum():
                lp += 1
            while lp<rp and not s[rp].isalnum():
                rp -= 1
            if s[lp].lower() != s[rp].lower():
                return False
            else:
                lp += 1
                rp -= 1
        return True