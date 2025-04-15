class BIT:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index: int, value: int) -> None:
        # BIT is 1-indexed.
        index += 1
        while index <= self.size:
            self.tree[index] += value
            index += index & -index
            
    def query(self, index: int) -> int:
        # return the sum of frequencies from index 0 to index (inclusive)
        res = 0
        index += 1
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        # build mapping for nums2, so that pos2[v] gives the index of v in nums2.
        pos2 = [0] * n
        for i, num in enumerate(nums2):
            pos2[num] = i
        
        # transform nums1 into an array that represents each value's position in nums2.
        arr = [pos2[num] for num in nums1]
        
        # count the number of smaller elements to the left for each position in arr.
        left_counts = [0] * n
        bit_left = BIT(n)
        for i in range(n):
            # For arr[i] being 0, there is no element smaller than it.
            left_counts[i] = bit_left.query(arr[i] - 1) if arr[i] > 0 else 0
            bit_left.update(arr[i], 1)
        
        # count the number of greater elements to the right for each position in arr.
        right_counts = [0] * n
        bit_right = BIT(n)
        for i in range(n - 1, -1, -1):
            # Count of elements to the right that are greater than arr[i] equals the
            # total elements seen so far (to the right) minus those that are less than or equal to arr[i].
            right_counts[i] = bit_right.query(n - 1) - bit_right.query(arr[i])
            bit_right.update(arr[i], 1)
        
        # for each index j as the middle element, add left_counts[j] * right_counts[j].
        total_triplets = 0
        for j in range(n):
            total_triplets += left_counts[j] * right_counts[j]
        
        return total_triplets
