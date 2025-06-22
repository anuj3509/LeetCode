class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS, stackT = [], []
        for index, val in enumerate(s):
            if s[index].isalpha():
                stackS.append(s[index])
            else:
                if stackS:
                    stackS.pop()
                else:
                    continue
                # stackS.pop() if stackS else continue
        
        for index, val in enumerate(t):
            if t[index].isalpha():
                stackT.append(t[index])
            else:
                if stackT:
                    stackT.pop()
                else:
                    continue

        return stackS == stackT