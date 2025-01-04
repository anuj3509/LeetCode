# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# # Recursive Approach [TC: O(n^2) , SC: O(n)]
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True

    #     left = self.dfs(root.left)
    #     right = self.dfs(root.right)
    #     if abs(left - right) > 1:
    #         return False
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)

    # def dfs(self, root):
    #     if not root:
    #         return 0
    #     return 1 + max(self.dfs(root.left), self.dfs(root.right))


# DFS approach bottom-up [TC: O(n) or Best case - O(log n), SC:O(h)]
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root: return [True, 0]   # 0 is the height of the tree, True if balanced

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
        