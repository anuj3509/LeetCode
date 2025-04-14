class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        
        # loop through every possible triplet (i, j, k) with i < j < k
        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) > a:    # early exit if the first condition fails
                    continue  # skipping this j since condition fails
                    
                for k in range(j + 1, n):
                    # checking the remaining two conditions for the triplet
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count