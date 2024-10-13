# Definition for singly-linked list.
from typing import Optional
import tools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # split the list into tow half

        left = head
        right = self.getMid(head)

        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        # merge them
        return self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = ListNode(left.val, None)
                left = left.next
            else:
                tail.next = ListNode(right.val, None)
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = [4, 2, 1, 3]
    head = tools.buildList(head)
    a = s.sortList(head)
    tools.printList(a)

    head = [-1, 5, 3, 4, 0]
    head = tools.buildList(head)
    a = s.sortList(head)
    tools.printList(a)

    head = []
    head = tools.buildList(head)
    a = s.sortList(head)
    tools.printList(a)
