# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if first and second tree are empty, trees are equal
        if not p and not q:
            return True

        # if first or second tree are empty, trees are not equal
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        # if both nodes p and q are non empty and values are same, 
        # call recursive function to check both left and right sub trees are equal
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        
