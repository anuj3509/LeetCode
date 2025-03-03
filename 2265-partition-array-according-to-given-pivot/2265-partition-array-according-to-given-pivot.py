class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        # TC: O(n) , SC: O(n)
        less = []   # array of elements which are less
        p = []      # pivot
        more = []   # array of elements which are more

        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                more.append(n)
            else:
                p.append(n)  
        return less + p + more

