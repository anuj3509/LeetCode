class Solution:
    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
    #     pair = [[p,s] for p,s in zip(position, speed)]
    #     stack = []

    #     for p, s in sorted(pair)[::-1]:  # Reverse Sorted Order
    #         stack.append((target - p) / s)  # Calculate ETA to append in stack
    #         # Decimal division because time can be decimal
    #         # Remember: '//' represents integer division and '/' represents decimal division
            
    #         # Check for collision only if we have atleast 2 cars in the stack
    #         # If time of the car on top of stack(stack[-1], i.e. one we recently added) is less than 
    #         # the time of the car below (stack[-2]), then it implies that they must have collided.
    #         if len(stack) >= 2 and stack[-1] <= stack[-2]:
    #             stack.pop() 
    #     return len(stack)


    def carFleet(self, target, position, speed):
        # Pair position and speed, sort by position descending (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd  # Time to reach target
            # If this car takes longer than the fleet ahead, it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # Else, it joins the fleet ahead (do nothing)
        return len(stack)