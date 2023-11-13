# 方法1：队和栈：一次遍历入栈，删掉第n个弹出来的
# 方法2：双指针：使用两个指针first和second同时对链表进行遍历，并且first比second超前n个节点。当first遍历到链表的末尾时，second 就恰好处于倒数第n个节点
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         nodes = []
#         cur = head
#         while cur != None:
#             nodes.append(cur)
#             cur = cur.next
#         nodes.append(cur)
#
#         nodes = nodes[0:len(nodes)-n-1] + nodes[len(nodes)-n:len(nodes)]
#         for i in range(0,len(nodes)-1):
#             nodes[i].next = nodes[i+1]
#         return nodes[0]

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fast = head
        slow = dummy

        i = 1
        while i <= cnt:
            fast = fast.next
            i += 1

        while fast != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head