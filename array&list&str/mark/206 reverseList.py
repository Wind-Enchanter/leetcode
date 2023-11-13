# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         val_list = []
#         cur = head
#         if cur == None:
#             return None
#         else:
#             while cur.next != None:
#                 val_list.append(cur.val)
#                 cur = cur.next
#             val_list.append(cur.val)
#
#             cur = head
#             while cur.next != None:
#                 cur.val = val_list.pop()
#                 cur = cur.next
#             cur.val = val_list.pop()
#         return head

# 方法1：两次遍历：一次遍历存储val，下一次遍历栈弹出更改节点val
# 方法2：迭代：用pre、cur、next指针操作，一次遍历完成反转
# 方法3：用栈实现（先进后出
# 方法4：

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = cur
        if cur.next == None:
            return head
        if cur.next.next == None:
            head = cur.next
            head.next = cur
            cur.next = None
            return head
        else:
            pre = cur
            cur = pre.next
            new_next = cur.next
            pre.next = None
            while new_next.next != None:
                cur.next = pre
                pre = cur
                cur = new_next
                new_next = new_next.next
            new_next.next = cur
            new_next.next.next = pre
            head = new_next
        return head


if __name__ == "__main__":
    my_so = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(my_so.reverseList(node1))
