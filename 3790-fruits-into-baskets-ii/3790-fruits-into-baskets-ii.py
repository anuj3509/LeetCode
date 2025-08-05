class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        # Greedy Approach - place each fruit in the first basket that meets the criteria

        # 1. loop through each fruit from left to right in the fruits array
        # 2. for every fruit, scan from left to right in the baskets array
        # 3. if a basket isn't used and its capacity is greater than or equal to the fruit
        #     i) place the fruit there
        #     ii) mark the basket as used
        #     iii) move to the next fruit
        # 4. keep count of fruits that are placed
        # 5. return the count of unplaced fruits (total - placed)
        
        b = len(baskets)
        used = [False] * b
        count = 0

        for fruit in fruits:
            found = False
            for j in range(b):
                if not used[j] and fruit <= baskets[j]:
                    used[j] = True
                    found = True
                    break
            if not found:
                count += 1
        return count

        # TC: O(n^2)  ;   SC: O(1)