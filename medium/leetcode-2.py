# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        c = 0
        cur = dummyHead
        while l1 and l2:
            curSum = l1.val + l2.val + c
            s = curSum
            if curSum >= 10:
                c = curSum // 10
                s = curSum % 10
            else:
                c = 0
            cur.next = ListNode(s)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            curSum = l1.val + c
            s = curSum
            if curSum >= 10:
                c = curSum // 10
                s = curSum % 10
            else:
                c = 0
            cur.next = ListNode(s)
            cur = cur.next
            l1 = l1.next

        while l2:
            curSum = l2.val + c
            s = curSum
            if curSum >= 10:
                c = curSum // 10
                s = curSum % 10
            else:
                c = 0
            cur.next = ListNode(s)
            cur = cur.next
            l2 = l2.next

        if c > 0:
            cur.next = ListNode(c)

        return dummyHead.next

    def addTwoNumbersV2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        cur = dummyHead
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            s = val % 10
            cur.next = ListNode(s)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next


if __name__ == '__main__':
    pass
