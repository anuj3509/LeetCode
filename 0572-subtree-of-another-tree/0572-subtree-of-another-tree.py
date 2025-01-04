# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

#   root = s    ;   subRoot = t

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t: return True   # if t is null, it can be a subtree of s
        if not s: return False  # if s is empty and t is non-empty, return False

        if self.sameTree(s, t):
            return True

        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))


    def sameTree(self, s, t) -> bool:
        # if first and second tree are empty, trees are equal
        if not s and not t:
            return True

        # if first and second tree are same, we compare their values
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
        
        return False    # if first or second tree are empty, trees are not equal

