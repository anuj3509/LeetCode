class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()   # sort the input array
        res = []

        def dfs(i, curr, total):
            
            if total == target:
                res.append(curr.copy())
                return

            if total > target or i == len(candidates):
                return

            # include numbers at candidates[i]
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])     # i+1 becaues we are not allowed repition of numbers
            curr.pop()      # make curr ready for other case where we don't append candidates[i]
            
            # skip numbers at candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1      # if duplicate found, increment pointer
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return res