# Definition for a binary tree node.
from collections import deque
import math


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        max_depth = self.maxDepth(root)
        res = []
        queue = deque()
        queue.append(root)
        for i in range(0, max_depth):
            for j in range(0, 2 ** i):
                temp_node = queue.popleft()
                if temp_node is None:
                    res.append("null")
                else:
                    res.append(str(temp_node.val))
                    queue.append(temp_node.left)
                    queue.append(temp_node.right)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split()
        if len(data) is 0:
            return None

        node_list = []
        for i in range(0, len(data)):
            if data[i] != 'null':
                node_list.append(TreeNode(data[i]))
            else:
                node_list.append(None)

        depth = int(math.log2(len(node_list) + 1))
        root = TreeNode(node_list[0])
        for i in range(0, int(depth)):
            first_num = 2 ** i - 1
            for j in range(0, 2 ** i):
                cur = first_num + j
                temp_node = node_list[cur]
                if temp_node is not None:
                    try:
                        temp_node.left = node_list[2 * cur + 1]
                        temp_node.right = node_list[2 * cur + 2]
                    except IndexError:
                        continue

        return node_list[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == "__main__":
    my_so = Codec()
    nodeA1 = TreeNode(1)
    nodeA2 = TreeNode(2)
    nodeA3 = TreeNode(3)
    nodeA4 = TreeNode(4)
    nodeA5 = TreeNode(5)
    nodeA6 = TreeNode(6)
    nodeA7 = TreeNode(7)
    nodeA1.left = nodeA2
    nodeA1.right = nodeA3
    nodeA3.left = nodeA4
    nodeA3.right = nodeA5
    nodeA4.left = nodeA6
    nodeA4.right = nodeA7
    #
    # nodeB1 = TreeNode(1)
    # nodeB2 = TreeNode(-4)
    # nodeB1.left = nodeB2

    code = my_so.serialize(nodeA1)

    decode = my_so.deserialize(code)

    print(code)
    print(decode)
