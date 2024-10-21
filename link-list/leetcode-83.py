# Definition for singly-linked list.
from typing import Optional
import tools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if head is None:
            return head
        if head.next is None:
            return head

        cur = head.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head

    def deleteDuplicatesV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next

            cur = cur.next
        return head


if __name__ == '__main__':
    s = Solution()
    head = [1, 1, 2]
    head = tools.buildList(head)
    a = s.deleteDuplicates(head)
    tools.printList(a)

    head = [1, 1, 2, 3, 3]
    head = tools.buildList(head)
    a = s.deleteDuplicates(head)
    tools.printList(a)
