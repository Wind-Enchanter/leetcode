
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         info = {}
#         cur = head
#         new_dum = Node(0, None, None)
#         while cur != None:
#             if cur not in info.keys():
#                 new_node = Node(cur.val, None, None)
#                 node_info = new_node
#                 info[cur] = node_info
#             else:
#                 new_node = info[cur]
#
#             if cur.next == None:
#                 new_node.next = None
#             elif cur.next not in info.keys():
#                 newer_node = Node(cur.next.val, None, None)
#                 node_info = newer_node
#                 info[cur.next] = node_info
#                 new_node.next = info[cur.next]
#             elif cur.next in info.keys():
#                 new_node.next = info[cur.next]
#
#             if cur.random == None:
#                 new_node.random = None
#             elif cur.random not in info.keys():
#                 newer_node = Node(cur.random.val, None, None)
#                 node_info = newer_node
#                 info[cur.random] = node_info
#                 new_node.random = info[cur.random]
#             elif cur.random in info.keys():
#                 new_node.random = info[cur.random]
#
#             cur = cur.next
#
#         if len(info.keys()) != 0:
#             new_dum.next = info[head]
#
#         return new_dum.next


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        info = {}
        cur = head
        while cur is not None:
            new_node = Node(cur.val, None, None)
            info[cur] = new_node
            cur = cur.next

        cur = head
        while cur is not None:
            if cur.next is not None:
                info[cur].next = info[cur.next]
            if cur.random is not None:
                info[cur].random = info[cur.random]
            cur = cur.next
        if len(info.keys()) != 0:
            return info[head]
        else:
            return None
