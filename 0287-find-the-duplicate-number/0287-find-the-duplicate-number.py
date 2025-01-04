class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # # Using a set to track seen numbers [TC = SC = O(n)]
        # visited = set()    # set
        # for i in nums:
        #     if i in visited:
        #         return i
        #     else:
        #         visited.add(i)

        # Using LL - Floyd's Hare and Tortoise Algorithm [TC: O(n), SC: O(1)]
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            