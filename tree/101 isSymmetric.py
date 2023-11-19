# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root is None:
#             return None
#         else:
#             root.left, root.right = root.right, root.left
#
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#
#         return root
#
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return True
#         queue1 = deque()
#         queue2 = deque()
#         queue1.append(root.left)
#         queue2.append(self.invertTree(root.right))
#         while len(queue1) is not 0:
#             temp_len = len(queue1)
#             for i in range(0, temp_len):
#                 temp1 = queue1.popleft()
#                 temp2 = queue2.popleft()
#                 if temp1 is not None and temp2 is not None and temp1.val != temp2.val:
#                     return False
#                 elif temp1 is not None and temp2 is None:
#                     return False
#                 elif temp2 is not None and temp1 is None:
#                     return False
#                 elif temp2 is None and temp1 is None:
#                     continue
#                 else:
#                     queue1.append(temp1.left)
#                     queue2.append(temp2.left)
#                     queue1.append(temp1.right)
#                     queue2.append(temp2.right)
#         if len(queue2) is not 0:
#             return False
#         return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue1 = deque()
        queue2 = deque()
        queue1.append(root.left)
        queue2.append(root.right)
        while len(queue1) is not 0:
            temp_len = len(queue1)
            for i in range(0,temp_len):
                temp1 = queue1.popleft()
                temp2 = queue2.popleft()
                if temp1 is not None and temp2 is not None and temp1.val != temp2.val:
                    return False
                elif temp1 is not None and temp2 is None:
                    return False
                elif temp2 is not None and temp1 is None:
                    return False
                elif temp2 is None and temp1 is None:
                    continue
                else:
                    queue1.append(temp1.left)
                    queue2.append(temp2.right)
                    queue1.append(temp1.right)
                    queue2.append(temp2.left)
        if len(queue2) is not 0:
            return False
        return True
