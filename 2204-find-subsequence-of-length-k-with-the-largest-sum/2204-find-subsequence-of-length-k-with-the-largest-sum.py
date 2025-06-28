class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = [(num, idx) for idx, num in enumerate(nums)]     # group number with its index
        
        # sorting descending, then take top k
        top_k = sorted(indexed_nums, key=lambda x: x[0], reverse=True)[:k]
        
        # sorting the top k by their original index to keep the subsequence order
        top_k_sorted = sorted(top_k, key=lambda x: x[1])
        
        return [num for num, idx in top_k_sorted]