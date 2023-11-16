# 方法1：递归DFS，每个节点的深度为max(l,r)+1
# 方法2：迭代BFS，计算层数

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root == None:
#             return 0
#         else:
#             return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
#

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque()
        res = 0
        queue.append(root)
        while len(queue) is not 0:
            temp_len = len(queue)
            for i in range(0, temp_len):
                temp_node = queue.popleft()
                if temp_node is not None:
                    queue.append(temp_node.left)
                    queue.append(temp_node.right)
                else:
                    continue
            res += 1
        return res-1
