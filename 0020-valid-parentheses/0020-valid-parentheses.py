class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closetoopen: 
                # 'in closetoopen' this checks the key of the hashmap
                # if stack checks if stack is not empty and we check
                # value at top is matching open parenthesis
                if stack and stack[-1] == closetoopen[c]:  
                     # 'closetoopen[c]' this checks the value of the key 'c' in the hashmap
                    stack.pop()
                else:
                    return False
            else:   #if we get an open paranthesis, add all of them to the stack
                stack.append(c)
            
        return True if not stack else False
