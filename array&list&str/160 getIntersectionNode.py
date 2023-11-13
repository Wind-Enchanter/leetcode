# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法1：两重循环遍历（超时间限制）
# 方法2：分别把链表AB压入栈，判断弹栈是否相同，返回不同元素的上一个节点
# 方法3：若相交，链表A： a+c, 链表B : b+c. a+c+b+c = b+c+a+c 。则会在公共处c起点相遇。若不相交，a +b = b+a 。因此相遇处是NULL（想不到）

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         curA = ListNode(0, headA)
#         curB = ListNode(0, headB)
#
#         while curA != None:
#             curB = ListNode(0, headB)
#             while curB != None and curB.next != curA:
#                 curB = curB.next
#             if curB != None and curB.next == curA:
#                 return curA
#             curA = curA.next
#
#         return None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA, listB = [], []
        curA, curB = headA, headB
        while curA != None:
            listA.append(curA)
            curA = curA.next
        while curB != None:
            listB.append(curB)
            curB = curB.next

        temp = ListNode(0, None)
        testA, testB = None, None
        if len(listA) + len(listB) <= 1:
            return temp.next
        while testA == testB:
            temp.next = testA
            if len(listA) >= 1 and len(listB) >= 1:
                testA, testB = listA.pop(), listB.pop()
            else:
                break
        return temp.next