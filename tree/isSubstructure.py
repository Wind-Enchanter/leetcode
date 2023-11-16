# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def isPart(self, A: TreeNode, B: TreeNode) -> bool:
        if A == None or B == None:
            return False
        queue1 = deque()
        queue2 = deque()
        queue1.append(B)
        queue2.append(A)
        while len(queue1) is not 0:
            temp_len = len(queue1)
            for i in range(0, temp_len):
                temp_node = queue1.popleft()
                test_node = queue2.popleft()
                if temp_node.val != test_node.val:
                    return False

                if temp_node.left is not None: queue1.append(temp_node.left)
                if temp_node.right is not None: queue1.append(temp_node.right)

                if test_node.left is not None and temp_node.left is not None:
                    queue2.append(test_node.left)
                if test_node.right is not None and temp_node.right is not None:
                    queue2.append(test_node.right)
                if test_node.left is None and temp_node.left is not None:
                    return False
                if test_node.right is None and temp_node.right is not None:
                    return False
                    # if
        return True

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A == None or B == None:
            return False
        queue = deque()
        queue.append(A)
        ready_list = []
        while len(queue) is not 0:
            temp_len = len(queue)
            for i in range(0, temp_len):
                temp_node = queue.popleft()
                if temp_node is not None:
                    queue.append(temp_node.left)
                    queue.append(temp_node.right)
                if temp_node is not None and B is not None and temp_node.val == B.val:
                    if self.isPart(temp_node, B):
                        return True
                    else:
                        continue
        return False

if __name__ == "__main__":
    my_so = Solution()
    nodeA1 = TreeNode(1)
    nodeA2 = TreeNode(0)
    nodeA3 = TreeNode(1)
    nodeA4 = TreeNode(-4)
    nodeA5 = TreeNode(-3)
    nodeA1.left = nodeA2
    nodeA1.right = nodeA3
    nodeA2.left = nodeA4
    nodeA2.left = nodeA5

    nodeB1 = TreeNode(1)
    nodeB2 = TreeNode(-4)
    nodeB1.left = nodeB2

    print(my_so.isPart(nodeA1,nodeB1))