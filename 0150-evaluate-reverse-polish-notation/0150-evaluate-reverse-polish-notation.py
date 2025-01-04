class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop() 
                # since order is important, we track the elements popped
                stack.append(b - a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                # since order is important, we track the elements popped
                stack.append(int(b / a))    # we use int to round it of to zero
            else:
                stack.append(int(c))

        return stack[0]
