class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []  
        for i in range(len(nums)):  
            for j in range(len(nums)):  
                if abs(i - j) <= k and nums[j] == key:  
                    # If the distance is within k and nums[j] is key
                    result.append(i)  # Add index i to the result
                    break  
        return result  