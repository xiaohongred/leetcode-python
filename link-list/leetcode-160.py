# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB  # 如果为空, 指向另一个链表的头部
            l2 = l2.next if l2 else headA  # 如果为空, 指向另一个链表的头部
        return l1

    def getIntersectionNodeV2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        len1, len2 = 0, 0
        # 算出长度
        while l1:
            len1 += 1
            l1 = l1.next
        while l2:
            len2 += 1
            l2 = l2.next

        # 对齐
        l1, l2 = headA, headB
        if len1 > len2:
            for i in range(len1 - len2):
                l1 = l1.next
        else:
            for i in range(len2 - len1):
                l2 = l2.next
        minLen = min(len1, len2)
        # 对齐之后遍历
        for i in range(minLen):
            if l1 == l2:
                return l1
            l1 = l1.next
            l2 = l2.next
        return None


if __name__ == '__main__':
    pass
