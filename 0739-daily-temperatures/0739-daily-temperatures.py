class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # initialized with 0 to avoid filling zeros at the end in case no greater temp is found 
        res = [0]*len(temperatures) 
        stack = []  # pair of temperatures and the index it occured at

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            stack.append([t,i])

        return res