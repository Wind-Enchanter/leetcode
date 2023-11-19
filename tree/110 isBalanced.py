# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.depth(root.left),self.depth(root.right))+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        test = self.depth(root.left) - self.depth(root.right)
        if test >= -1 and test <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False