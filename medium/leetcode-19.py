# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        fast, slow = dummyHead, dummyHead
        for i in range(n):
            if fast is not None:
                fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        if slow.next is not None:
            slow.next = slow.next.next
        else:
            slow.next = None
        return dummyHead.next

    def removeNthFromEndV2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


if __name__ == '__main__':
    pass
