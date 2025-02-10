class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        delete_cnt = 0

        def isdigit(c):
            return ord("0") <= ord(c) <= ord("9")
        
        for i in reversed(range(len(s))):
            # if s[i].isdigit():  # this is if you want to use the built-in isdigit() function
            if isdigit(s[i]):
                delete_cnt += 1
            elif delete_cnt:    # not a digit but our delete count is positive
                delete_cnt -= 1
            else:               # not a digit but our delete count is 0
                res.append(s[i])

    # since we are going through the string in reverse order, our res is also generated from reverse
        return "".join(res[::-1])