# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Return: (LCA, height)
        def dfs(node):
            if not node:
                return (None, 0)

            leftnode, leftheight = dfs(node.left)
            rightnode, rightheight = dfs(node.right)

            if leftheight == rightheight:
                return node, 1 + leftheight
            elif leftheight > rightheight:
                return leftnode, leftheight + 1
            else:
                return rightnode, rightheight + 1
        
        node, _ = dfs(root)
        return node