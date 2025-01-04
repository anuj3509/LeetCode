class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # maxarea = 0
        # stack = []  # pair: index, heights

        # for i, h in enumerate(heights):
        #     # start index is 'i', because at the start we don't know if we can extend it backwards
        #     start = i   
        #     while stack and stack[-1][1] > h:
        #         index, height = stack.pop()
        #         maxarea = max(maxarea, height*(i - index))
        #         # pushing the start index back if the height popped is greater than the current height we are visiting
        #         start = index
        #     stack.append((start, h))

        # # Remember, after the above for loop, there may be values in the stack. So
        # # we will calculate the max area for those remaining values

        # for i, h in stack:
        #     maxarea = max(maxarea, h*(len(heights) - i))
        # return maxarea



        # Stack to store indices
        stack = []
        max_area = 0
        n = len(heights)
        
        # Append a zero height to handle remaining stack bars
        heights.append(0)
        
        for i in range(len(heights)):
            # Process and calculate area for taller heights in the stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Height of the bar
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)  # Add current index to the stack
        
        return max_area
