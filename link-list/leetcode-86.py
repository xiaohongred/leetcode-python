# Definition for singly-linked list.
from typing import Optional
import tools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        pl = left
        right = ListNode()
        pr = right

        while head:
            tmp = head.next
            head.next = None
            if head.val < x:
                pl.next = head
                pl = pl.next
            else:
                pr.next = head
                pr = pr.next
            head = tmp

        pl = left
        while pl.next:
            pl = pl.next
        pl.next = right.next

        return left.next

    def partitionV2(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        ltail.next = right.next
        rtail.next = None
        return left.next


if __name__ == '__main__':
    s = Solution()
    head = [1, 4, 3, 2, 5, 2]
    head = tools.buildList(head)
    x = 3
    a = s.partition(head, x)
    tools.printList(a)

    head = [2, 1]
    head = tools.buildList(head)
    x = 2
    a = s.partition(head, x)
    tools.printList(a)

    head = [1, 4, 3, 2, 5, 2]
    head = tools.buildList(head)
    x = 3
    a = s.partitionV2(head, x)
    tools.printList(a)

    head = [2, 1]
    head = tools.buildList(head)
    x = 2
    a = s.partitionV2(head, x)
    tools.printList(a)
