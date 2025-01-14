class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []    # to store the final answer with all combinations

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # if we choose to append this number
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])   # including the number in candidates at pointer i

            # if we choose to not append this number and move on to the next one
            curr.pop()
            dfs(i + 1, curr, total)    # including the number in nums at pointer i, moving on to next number

        dfs(0, [], 0)   # 0 index, empty array result, 0 target 
        return res        