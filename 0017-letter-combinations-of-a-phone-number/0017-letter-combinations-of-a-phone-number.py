class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitmap = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "qprs",
                    "8": "tuv",
                    "9": "wxyz" }

        def backtrack(i, currstring):
            if len(currstring) == len(digits) :     # or i >= len(digits)
                res.append(currstring)
                return

            for c in digitmap[digits[i]]:
                backtrack(i + 1, currstring + c)

        if digits:      # call the backtracking function if the input digit string is non empty
            backtrack(0, "")

        return res