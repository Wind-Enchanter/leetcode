# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        res = []
        queue.append(root)
        while len(queue) is not 0:
            temp_len = len(queue)
            temp = []
            for i in range(0, temp_len):
                temp_node = queue.popleft()
                if temp_node is not None:
                    temp.append(temp_node.val)
                    queue.append(temp_node.left)
                    queue.append(temp_node.right)
            res.append(temp)

        return res[:-1]