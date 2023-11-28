# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        lenB = 0
        pA = headA
        pB = headB
        while pA is not None:
            lenA += 1
            pA = pA.next

        while pB is not None:
            lenB += 1
            pB = pB.next

        pA = headA
        pB = headB
        if lenA > lenB:
            diff = lenA - lenB
            while diff > 0 and pA is not None:
                pA = pA.next
                diff -= 1
        else:
            diff = lenB - lenA
            while diff > 0 and pB is not None:
                pB = pB.next
                diff -= 1

        while pA is not None and pB is not None:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next

        return None

    def getIntersectionNodeV2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1


if __name__ == '__main__':
    node = ListNode(12)
    print(node)
