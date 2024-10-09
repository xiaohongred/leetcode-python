# Definition for singly-linked list.
from typing import Optional
import tools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        while n:
            fast = fast.next
            n -= 1

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 3, 4, 5]
    n = 2
    head = tools.buildList(head)
    a = s.removeNthFromEnd(head, n)
    tools.printList(a)

    head = [1]
    n = 1
    head = tools.buildList(head)
    a = s.removeNthFromEnd(head, n)
    tools.printList(a)

    head = [1, 2]
    n = 1
    head = tools.buildList(head)
    a = s.removeNthFromEnd(head, n)
    tools.printList(a)
